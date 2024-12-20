from typing import List, Tuple


def read_input(
    file_path: str,
) -> Tuple[List[List[int]], Tuple[int, int], Tuple[int, int]]:
    graph = []
    starting_p = (0, 0)
    target_p = (0, 0)
    with open(file_path, "r") as file:
        for i, line in enumerate(file):
            graph.append(list(line.strip()))
            if "S" in line:
                starting_p = (i, line.index("S"))
            if "E" in line:
                target_p = (i, line.index("E"))
    return graph, starting_p, target_p


def bfs_fill(graph: List[List[int]], starting_p: Tuple[int, int]) -> List[List[int]]:
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    queue = [(0, *starting_p)]
    r = [[-1 for _ in range(len(graph[0]))] for _ in range(len(graph))]
    r[starting_p[0]][starting_p[1]] = 0
    while queue:
        d, x, y = queue.pop(0)
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (
                0 <= nx < len(graph)
                and 0 <= ny < len(graph[0])
                and graph[nx][ny] != "#"
                and r[nx][ny] == -1
            ):
                r[nx][ny] = d + 1
                queue.append((d + 1, nx, ny))
    return r

def count_position_shortcuts(
    graph: List[List[int]],
    s_distances: List[List[int]],
    e_distances: List[List[int]],
    i: int,
    j: int,
    threshold: int = 102,
):
    directions = [(0, 1), (1, 0)]
    total = 0
    for d in directions:
        x1, y1 = i + d[0], j + d[1]
        x2, y2 = i - d[0], j - d[1]
        if (
            0 <= x1 < len(graph)
            and 0 <= y1 < len(graph[0])
            and 0 <= x2 < len(graph)
            and 0 <= y2 < len(graph[0])
        ):
            if s_distances[x1][y1] != -1 and e_distances[x2][y2] != -1:
                if (
                    abs(s_distances[x1][y1] - s_distances[x2][y2])
                    >= threshold
                    and abs(e_distances[x1][y1] - e_distances[x2][y2])
                    >= threshold
                    and (s_distances[x1][y1]-s_distances[x2][y2]) * (e_distances[x1][y1]-e_distances[x2][y2]) < 0
                ):
                    total += 1

    return total


def count_shortcuts(
    graph: List[List[int]], starting_p: Tuple[int, int], target_p: Tuple[int, int]
) -> int:
    s_distances = bfs_fill(graph, starting_p)
    e_distances = bfs_fill(graph, target_p)
    total = 0
    for i, row in enumerate(graph):
        for j, cell in enumerate(row):
            if cell == "#":
               total += count_position_shortcuts(graph, s_distances, e_distances, i, j) 
    return total

def conditions_for_shortcut(graph: List[List[int]], 
    s_distances: List[List[int]],
    e_distances: List[List[int]],
    pos1: Tuple[int, int],
    pos2: Tuple[int, int],
    threshold: int = 100) -> bool:
    x1, y1 = pos1
    x2, y2 = pos2
    d = abs(x1-x2)+abs(y1-y2)
    if d > 20 or d < 2:
        return False
    if graph[x1][y1] == "#" or graph[x2][y2] == "#":
        return False
    if s_distances[x1][y1] - s_distances[x2][y2] - d < threshold:
        return False
    if e_distances[x2][y2] - e_distances[x1][y1] - d < threshold:
        return False
    return True

    

def part2(graph: List[List[int]], starting_p: Tuple[int, int], target_p: Tuple[int, int]) -> int:
    s_distances = bfs_fill(graph, starting_p)
    e_distances = bfs_fill(graph, target_p)
    total = 0
    for i, row in enumerate(graph):
        for j, cell in enumerate(row):
            for i2 in range(max(0, i-21), min(len(graph), i+21)):
                margin = 20 - abs(i - i2) +1
                for j2 in range(max(0, j-margin), min(len(graph[0]), j+margin)):
                    if conditions_for_shortcut(graph, s_distances, e_distances, (i,j), (i2,j2)):
                        total += 1
    return total

if __name__ == "__main__":
    graph, starting_p, target_p = read_input("inputs/input_20.txt")
    print(f"Part 1: {count_shortcuts(graph, starting_p, target_p)}")
    print(f"Part 2: {part2(graph, starting_p, target_p)}")