import time
from collections import defaultdict
from typing import List, Tuple

def read_input() -> List[Tuple[str, str]]:
    with open("inputs/input_23.txt") as f:
        pair_list = []
        for line in f.readlines():
            x,y = line.strip().split("-")
            pair_list.append((x, y))
    return pair_list

def make_graph(pair_list: List[Tuple[str, str]]) -> dict:
    graph = defaultdict(list)
    for x, y in pair_list:
        graph[x].append(y)
        graph[y].append(x)
    return graph

def part1(graph):
    r = set()
    for key, value in graph.items():
        if key.startswith("t"):
            for i, v1 in enumerate(value[:-1]):
                for j, v2 in enumerate(value[i+1:]):
                    if v1 in graph[v2]:
                        r.add(tuple(sorted([key, v1, v2])))
    return len(r)

def part2(pair_list, graph):
    components = []
    for x,y in pair_list:
        b_in = False
        for component in components:
            x_in, y_in = False, False
            if all([c in graph[x] for c in component]):
                x_in = True
                component.append(x)
            if all([c in graph[y] for c in component]):
                y_in = True
                component.append(y)
            if x_in and y_in:
                b_in = True
        if not b_in:
            components.append([x,y])
    components = sorted(components, key=lambda x: len(x), reverse=True)
    return ",".join(sorted(components[0]))
        
            
    

if __name__ == "__main__":
    t0 = time.time()
    pair_list = read_input()
    graph = make_graph(pair_list)
    print(f"part 1; {part1(graph)}")
    print(f"part 2; {part2(pair_list, graph)}")
    print(f"executed in {time.time()-t0} seconds.")