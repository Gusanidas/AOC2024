from collections import defaultdict
from typing import List, Tuple, Dict, Set
from heapq import heappush, heappop


def dijkstra(
    graph: List[List[int]], starting_p: Tuple[int, int], target_p: Tuple[int, int]
) -> int:
    starting_pos = (0, *starting_p)
    pq: List[Tuple[int, Tuple[int, int, int]]] = [(0, starting_pos)]
    dic: Dict[Tuple[int, int, int], int] = {starting_pos: 0}
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    while pq:
        score, (d, x, y) = heappop(pq)
        if (x, y) == target_p:
            return score
        dx, dy = directions[d]
        nx, ny = x + dx, y + dy
        if graph[nx][ny] != "#" and 0 <= nx < len(graph) and 0 <= ny < len(graph[0]):
            if (d, nx, ny) not in dic or dic[(d, nx, ny)] > score + 1:
                dic[(d, nx, ny)] = score + 1
                heappush(pq, (score + 1, (d, nx, ny)))
        turn_clockwise = (d + 1) % 4
        if (turn_clockwise, x, y) not in dic or dic[
            (turn_clockwise, x, y)
        ] > score + 1000:
            dic[(turn_clockwise, x, y)] = score + 1000
            heappush(pq, (score + 1000, (turn_clockwise, x, y)))
        turn_counter_clockwise = (d + 3) % 4
        if (turn_counter_clockwise, x, y) not in dic or dic[
            (turn_counter_clockwise, x, y)
        ] > score + 1000:
            dic[(turn_counter_clockwise, x, y)] = score + 1000
            heappush(pq, (score + 1000, (turn_counter_clockwise, x, y)))
    return -1


def get_all_ancestors(
    parents: Dict[Tuple[int, int, int], List[Tuple[int, int, int]]],
    target_p: Tuple[int, int, int],
    good_places: Set[Tuple[int, int, int]],
) -> Set[Tuple[int, int, int]]:
    result = set([target_p])
    #print(f"target_p: {target_p},")
    if target_p in good_places:
        return set()
    for parent in parents[target_p]:
        if parent in good_places or parent in result:
            continue
        result.add(parent)
        result.update(get_all_ancestors(parents, parent, good_places))
    return result


def dijkstra_paths(
    graph: List[List[int]], starting_p: Tuple[int, int], target_p: Tuple[int, int]
) -> int:
    starting_pos = (0, *starting_p)
    pq: List[Tuple[int, Tuple[int, int, int]]] = [(0, starting_pos)]
    dic: Dict[Tuple[int, int, int], int] = {starting_pos: 0}
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    parents = defaultdict(lambda: [])
    good_places = set()
    shorted_length = None
    while pq:
        score, (d, x, y) = heappop(pq)
        if (x, y) == target_p:
            if shorted_length is None or score <= shorted_length:
                shorted_length = score
                good_places.update(get_all_ancestors(parents, (d, x, y), good_places))
        dx, dy = directions[d]
        nx, ny = x + dx, y + dy
        if graph[nx][ny] != "#" and 0 <= nx < len(graph) and 0 <= ny < len(graph[0]):
            if (d, nx, ny) not in dic or dic[(d, nx, ny)] >= score + 1:
                dic[(d, nx, ny)] = score + 1
                heappush(pq, (score + 1, (d, nx, ny)))
                parents[(d, nx, ny)].append((d, x, y))
        turn_clockwise = (d + 1) % 4
        if (turn_clockwise, x, y) not in dic or dic[
            (turn_clockwise, x, y)
        ] >= score + 1000:
            dic[(turn_clockwise, x, y)] = score + 1000
            heappush(pq, (score + 1000, (turn_clockwise, x, y)))
            parents[(turn_clockwise, x, y)].append((d, x, y))
        turn_counter_clockwise = (d + 3) % 4
        if (turn_counter_clockwise, x, y) not in dic or dic[
            (turn_counter_clockwise, x, y)
        ] >= score + 1000:
            dic[(turn_counter_clockwise, x, y)] = score + 1000
            heappush(pq, (score + 1000, (turn_counter_clockwise, x, y)))
            parents[(turn_counter_clockwise, x, y)].append((d, x, y))

    return len(set([(x,y) for _,x,y in good_places]))


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


def main() -> None:
    graph, starting_p, target_p = read_input("inputs/input_16.txt")
    result = dijkstra(graph, starting_p, target_p)
    print(f"Part 1 -- Result: {result}")
    result = dijkstra_paths(graph, starting_p, target_p)
    print(f"Part 2 -- Result: {result}")


if __name__ == "__main__":
    main()
