from typing import List, Dict, Tuple, Set
from collections import defaultdict, deque


def topological_sort(
    graph: Dict[int, Set[int]], indegree_map: Dict[int, int]
) -> Dict[int, int]:
    r = []
    q = deque()
    for node, indegree in indegree_map.items():
        if indegree == 0:
            q.append(node)

    while q:
        curr_node = q.popleft()
        r.append(curr_node)
        for neigh in graph[curr_node]:
            indegree_map[neigh] -= 1
            if indegree_map[neigh] == 0:
                q.append(neigh)

    return {node: idx for idx, node in enumerate(r)}


def create_graph(
    pairs: List[Tuple[int, int]]
) -> Tuple[Dict[int, Set[int]], Dict[int, int]]:
    graph = defaultdict(set)
    indegree_map = defaultdict(int)
    for node1, node2 in pairs:
        indegree_map[node2] += 1
        indegree_map[node1] += 0
        graph[node1].add(node2)
    return graph, indegree_map


def follows_order(update: List[int], graph: Dict[int, Set[int]]):
    seen = set()
    for node in update:
        if len(graph[node] & seen) > 0:
            return False
        seen.add(node)
    return True


def part_one():
    with open("inputs/input_day5.txt") as f:
        total, pairs, updates = 0, [], []
        for line in f.readlines():
            if "|" in line:
                pairs.append(tuple(map(int, line.split("|"))))
            elif "," in line:
                updates.append(list(map(int, line.split(","))))
        graph, _ = create_graph(pairs)
        for update in updates:
            if follows_order(update, graph):
                total += update[len(update) // 2]
    return total


def part_two():
    with open("inputs/input_day5.txt") as f:
        total, pairs, updates = 0, [], []
        for line in f.readlines():
            if "|" in line:
                pairs.append(tuple(map(int, line.split("|"))))
            elif "," in line:
                updates.append(list(map(int, line.split(","))))

        main_graph, _ = create_graph(pairs)
        for update in updates:
            if not follows_order(update, main_graph):
                relevant_pairs = [
                    (a, b) for a, b in pairs if a in update and b in update
                ]
                graph, indegree_map = create_graph(relevant_pairs)
                top_order = topological_sort(graph, indegree_map)
                update.sort(key=lambda x: top_order.get(x, -1))
                total += update[len(update) // 2]
    return total


if __name__ == "__main__":
    p1 = part_one()
    print(f"part one = {p1}")
    p2 = part_two()
    print(f"part two = {p2}")
