import time
from typing import List, Tuple
from functools import lru_cache
t0 = time.time()

@lru_cache(maxsize=8192)
def is_design_possible(design: str, towels: Tuple[str]) -> bool:
    for towel in towels:
        if design == towel:
            return True
        if design.startswith(towel):
            if is_design_possible(design[len(towel):], towels):
                return True
    return False


@lru_cache(maxsize=8192)
def number_of_combinations(design: str, towels: Tuple[str]) -> int:
    if design == "":
        return 1
    result = 0
    for towel in towels:
        if design.startswith(towel):
            result += number_of_combinations(design[len(towel):], towels)
    return result

def read_input() -> Tuple[List[str], List[str]]:
    with open("inputs/input_19.txt") as f:
        designs = []
        towels = []
        for i, line in enumerate(f.readlines()):
            if i == 0:
                towels = [l.strip() for l in line.strip().split(",")]
            elif i>2:
                designs.append(line.strip())
    return towels, designs


if __name__ == "__main__":
    towels, designs = read_input()
    towels = tuple(towels)
    result = sum([is_design_possible(design, towels) for design in designs])
    print(f"Part 1 -- Result: {result}")
    result_part2 = sum([number_of_combinations(design, towels) for design in designs])
    print(f"Part 2 -- Result: {result_part2}")