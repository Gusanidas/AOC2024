from typing import List, Tuple, Optional, Set


def is_out(grid: List[List[str]], nx: int, ny: int) -> bool:
    return 0 > nx or len(grid) <= nx or 0 > ny or len(grid[0]) <= ny


def next_move(
    grid: List[List[str]], d: int, px: int, py: int
) -> Tuple[int, Optional[Tuple[int, int]]]:
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    dx, dy = directions[d]
    nx, ny = px + dx, py + dy
    if is_out(grid, nx, ny):
        return d, None
    if grid[nx][ny] == "#":
        d = (d + 1) % 4
        nx, ny = px, py
    return d, (nx, ny)


def travel_path(grid: List[List[str]], gx: int, gy: int):
    path, pos, d = [], (gx, gy), 0
    while pos:
        d, pos = next_move(grid, d, *pos)
        path.append(pos)
    return len(set(path)) - 1


def is_loop(
    grid: List[List[str]],
    path: Set[Tuple[int, int, int]],
    d: int,
    pos: Optional[Tuple[int, int]],
) -> bool:
    while pos:
        e = (d, *pos)
        if e in path:
            return True
        path.add(e)
        d, pos = next_move(grid, d, *pos)
    return False


def find_loops(grid: List[List[str]], gx: int, gy: int) -> int:
    path, loops = set(), set()
    pos, d = (gx, gy), 0
    while pos:
        next_d, next_pos = next_move(grid, d, *pos)
        if next_pos and next_pos != pos and next_pos not in loops:
            npx, npy = next_pos
            grid[npx][npy] = "#"
            if is_loop(grid, set(), 0, (gx, gy)):
                loops.add(next_pos)
            grid[npx][npy] = "."
        path.add((d, *pos))
        d, pos = next_d, next_pos
    return len(loops)


def solve():
    with open("inputs/input_day6.txt") as f:
        grid = []
        possible_guards = [">", "v", "^", "<"]
        gp = None
        for i, line in enumerate(f.readlines()):
            line = line.strip()
            if gp is None:
                for guard in possible_guards:
                    if guard in line:
                        gp = (i, line.find(guard))
            grid.append(list(line))

        gx, gy = gp if gp else (0, 0)
        grid[gx][gy] = "."
        first_part = travel_path(grid, gx, gy)
        second_part = find_loops(grid, gx, gy)
    print(f"part 1 is {first_part}")
    print(f"part 2 is {second_part}")


if __name__ == "__main__":
    solve()
