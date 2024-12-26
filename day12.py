from collections import defaultdict
from typing import List, Tuple

def parse_input() -> List[List[str]]:
    grid = []
    with open('inputs/input_12.txt') as f:
        for line in f.readlines():
            grid.append(list(line.strip()))
    return grid

def get_perimeter1(visited: set) -> int:
    perimeter = 0
    for x, y in visited:
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            new_x, new_y = x + dx, y + dy
            if (new_x, new_y) not in visited:
                perimeter += 1
    return perimeter

def get_perimeter2(visited) -> int:
    hedges, vedges = defaultdict(list), defaultdict(list)
    perimeter = 0
    for x, y in visited:
        for new_x, new_y in [(x+1, y), (x-1, y)]:
            if (new_x, new_y) not in visited:
                hedges[(x+2*new_x)/3].append(y)
        for new_x, new_y in [(x, y+1), (x, y-1)]:
            if (new_x, new_y) not in visited:
                vedges[(y+2*new_y)/3].append(x)

    for k, v in hedges.items():
        perimeter += 1
        v = sorted(v)
        for i in range(1, len(v)):
            if v[i] - v[i-1] > 1:
                perimeter += 1
    for k, v in vedges.items():
        perimeter += 1
        v = sorted(v)
        for i in range(1, len(v)):
            if v[i] - v[i-1] > 1:
                perimeter += 1

    return perimeter

def get_group(grid: List[List[str]], start: Tuple[int, int], part1: bool = True) -> Tuple[int, int, set]:
    visited = set()
    q = [start]
    while q:
        x, y = q.pop()
        if (x, y) in visited:
            continue
        visited.add((x, y))
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and grid[new_x][new_y] == grid[x][y]:
                q.append((new_x, new_y))
                

    area = len(visited)
    if part1:
        perimeter = get_perimeter1(visited)
    else:
        perimeter = get_perimeter2(visited)
    return area, perimeter, visited 

def total_price(grid: List[List[str]], part1: bool = True) -> int:
    groups = []
    visited = set()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i, j) not in visited:
                area, perimeter, group = get_group(grid, (i, j), part1)
                visited |= group
                groups.append((area, perimeter))

    return sum([area*perimeter for area, perimeter in groups])

def part1():
    grid = parse_input()
    return total_price(grid, True)

def part2():
    grid = parse_input()
    return total_price(grid, False)

if __name__ == '__main__':
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
