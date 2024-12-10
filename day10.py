from typing import List, Tuple
from collections import deque


def score_trailheads(grid: List[List[int]], is_part_one: bool) -> int:
    trail_heads = []
    for i, row in enumerate(grid):
        for j, element in enumerate(row):
            if element == 0:
                trail_heads.append((i, j))
    if is_part_one:
        return sum(
            [score_single_trailhead_one(trail_head, grid) for trail_head in trail_heads]
        )
    else:
        return sum(
            [score_single_trailhead_two(trail_head, grid) for trail_head in trail_heads]
        )


def score_single_trailhead_one(
    trail_head: Tuple[int, int], grid: List[List[int]]
) -> int:
    q = deque([trail_head])
    seen = set()
    total = 0
    while q:
        cx, cy = q.popleft()
        curr_value = grid[cx][cy]
        # print(f"total = {total}, nx = {cx}, ny = {cy}, curr_value = {curr_value}")
        total += curr_value == 9
        neigh = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dx, dy in neigh:
            nx, ny = cx + dx, cy + dy
            if (
                0 <= nx < len(grid)
                and 0 <= ny < len(grid[0])
                and grid[nx][ny] == curr_value + 1
                and (nx, ny) not in seen
            ):
                seen.add((nx, ny))
                q.append((nx, ny))
    return total


def score_single_trailhead_two(
    trail_head: Tuple[int, int], grid: List[List[int]]
) -> int:
    total = 0
    cx, cy = trail_head
    curr_value = grid[cx][cy]
    if curr_value == 9:
        return 1
    neigh = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for dx, dy in neigh:
        nx, ny = cx + dx, cy + dy
        if (
            0 <= nx < len(grid)
            and 0 <= ny < len(grid[0])
            and grid[nx][ny] == curr_value + 1
        ):
            total += score_single_trailhead_two((nx, ny), grid)
    return total


def solve():
    with open("inputs/input_day10.txt") as f:
        grid = []
        for line in f.readlines():
            grid.append([int(x) for x in list(line.strip())])
        print(f"grid = {grid}")
        part_one = score_trailheads(grid, True)
        print(f"part_one = {part_one}")
        part_two = score_trailheads(grid, False)
        print(f"part_two = {part_two}")


if __name__ == "__main__":
    solve()
