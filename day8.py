from collections import defaultdict

def get_antinodes(a1, a2):
    x1, y1 = a1
    x2, y2 = a2
    direction = (x2 - x1, y2 - y1)
    antinode1 = (x2 + direction[0], y2 + direction[1])
    antinode2 = (x1 - direction[0], y1 - direction[1])
    return antinode1, antinode2

def get_antinodes2(a1, a2, width, height):
    antinodes = set()
    x1, y1 = a1
    x2, y2 = a2
    direction = (x2 - x1, y2 - y1)
    for k in range(0, max(width, height)):
        antinode = (x1 + k*direction[0], y1 + k*direction[1])
        if antinode[0] >= 0 and antinode[1] >= 0 and antinode[0] < height and antinode[1] < width:
            antinodes.add(antinode)
        else:
            break
    for k in range(0, max(width, height)):
        antinode = (x2 - k*direction[0], y2 - k*direction[1])
        if antinode[0] >= 0 and antinode[1] >= 0 and antinode[0] < height and antinode[1] < width:
            antinodes.add(antinode)
        else:
            break
    return antinodes

def process_input(file_path, part1=True):
    antinodes = set()
    anntena_locations = defaultdict(list)
    width = 0
    height = 0
    with open(file_path, "r") as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            line = line.strip()
            height = i+1
            width = len(line)
            for j, c in enumerate(line):
                if c != '.':
                    anntena_locations[c].append((i, j))
    
    for k, v in anntena_locations.items():
        if len(v)>1:
            for i, vv in enumerate(v[:-1]):
                for j in range(i+1, len(v)):
                    if part1:
                        a1, a2 = get_antinodes(vv, v[j])
                        if a1[0] >= 0 and a1[1] >= 0 and a1[0] < height and a1[1] < width:
                            antinodes.add(a1)
                        if a2[0] >= 0 and a2[1] >= 0 and a2[0] < height and a2[1] < width:
                            antinodes.add(a2)
                    else:
                        antinodes.update(get_antinodes2(vv, v[j], width, height))
    return antinodes


if __name__ == "__main__":
    antinodes = process_input("inputs/input_8.txt")
    print(f"Part 1: {len(antinodes)}")
    antinodes = process_input("inputs/input_8.txt", part1=False)
    print(f"Part 2: {len(antinodes)}")