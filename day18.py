from typing import List, Tuple, Set
from collections import deque


def bfs(obstacles: Set[Tuple[int, int]]) -> int:
    x, y = 0, 0
    visited = set([(x, y)])
    queue = deque([(x, y, 0)])
    neigh = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    while queue:
        x, y, d = queue.popleft()
        if (x, y) == (70, 70):
            return d
        for dx, dy in neigh:
            nx, ny = x+dx, y+dy
            if (nx, ny) not in visited and (nx, ny) not in obstacles and 0<=nx<=70 and 0<=ny<=70:
                visited.add((nx, ny))
                queue.append((nx, ny, d+1))
    return -1

def read_input() -> List[Tuple[int, int]]:
    r = []
    with open("inputs/input_18.txt") as f:
        for line in f:
            r.append(tuple(map(int,line.strip().split(","))))
    return r
        

def part1() -> int:
    obstacles = set(read_input()[:1024])
    return bfs(obstacles)

def part2() -> Tuple[int, int]:
    obstacles = read_input()
    lo, hi = 1024, len(obstacles)
    while lo < hi:
        mid = (lo + hi) // 2
        if bfs(set(obstacles[:mid])) == -1:
            hi = mid
        else:
            lo = mid+1
    return obstacles[lo-1]

if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")