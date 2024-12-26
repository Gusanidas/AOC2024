from typing import List, Dict

def evolve_stone(stone: int) -> List[int]:
    if stone == 0:
        return [1]
    elif len(str(stone))%2 == 0:
        stone1, stone2 = str(stone)[:len(str(stone))//2], str(stone)[len(str(stone))//2:]
        return [int(x) for x in [stone1, stone2]]
    else:
        return [2024*stone]

def blink(stones: Dict[int, int]) -> Dict[int, int]:
    new_stones = {}
    for stone, v in stones.items():
        expanded_stones = evolve_stone(stone) 
        for expanded_stone in expanded_stones:
            if expanded_stone in new_stones:
                new_stones[expanded_stone] += v
            else:
                new_stones[expanded_stone] = v
    return new_stones

def process_input(filename: str) -> Dict[int, int]:
    with open(filename) as f:
        rl =  [int(x) for x in f.readline().strip().split(" ")]
        stones = {}
        for x in rl:
            stones[x] = stones.get(x, 0) + 1
    return stones

def count_total_length(stones: Dict[int, int]) -> int:
    return sum(stones.values())


if __name__ == '__main__':
    stones = process_input("inputs/input_11.txt")
    for i in range(25):
        stones = blink(stones)
    print(f"Part 1: {count_total_length(stones)}")
    for i in range(50):
        stones = blink(stones)
    print(f"Part 2: {count_total_length(stones)}")