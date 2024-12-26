from typing import List

def read_lock(lines: List[str]):
    r = [0 for _ in lines[0]]
    for line in lines:
        for i, c in enumerate(line.strip()):
            if c == '#':
                r[i] += 1

    return r

def read_input(filename: str):
    locks, keys = [], []
    curr = []
    with open(filename) as f:
        lines = f.readlines() + ['']
        for line in lines:
            if len(line.strip()) == 0:
                if len(curr) > 0 and curr[0].startswith('#'):
                    locks.append(read_lock(curr))
                else:
                    keys.append(read_lock(curr[::-1]))
                curr = []
            else:
                curr.append(line.strip())
    return locks, keys


def match(key, lock):
    h = 8
    for i, (k, l) in enumerate(zip(key, lock)):
        if h <= k+l:
            return False
    return True

def part1():
    locks, keys = read_input("inputs/input_25.txt")
    total = 0
    print(f"Locks: {locks}")
    print(f"Keys: {keys}")
    for i, lock in enumerate(locks):
        for j, key in enumerate(keys):
            if match(key, lock):
                print(f"Match at {i} {j}")
                total += 1
    print(f"Total matches: {total}")

if __name__ == '__main__':
    part1()