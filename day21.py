
keypad1 = [" ^A", "<v>"]
keypad2 = ["789", "456", "123", " 0A"]

def fewest_presses_for_sequence(sequence, pairs2shortest):
    starting = "A"
    total = 0
    for c in sequence:
        total += pairs2shortest[(starting, c)]
        starting = c
    return total


def get_num_presses_map(num_robots):
    keypad1 = [" ^A", "<v>"]
    key_coords = {key: (i, j) for i, row in enumerate(keypad1) for j, key in enumerate(row)}
    num_presses_map = {(key1, key2): 1 for key1 in key_coords for key2 in key_coords}
    for i in range(num_robots):
        new_num_presses_map = {}
        for key1, key2 in num_presses_map.keys():
            x1, y1 = key_coords[key1]
            x2, y2 = key_coords[key2]
            ver_moves = ["v" if x2 > x1 else "^"] * abs(x2 - x1)
            hor_moves = [">" if y2 > y1 else "<"] * abs(y2 - y1)
            hor_first = fewest_presses_for_sequence(hor_moves + ver_moves + ["A"], num_presses_map) if (x1, y2) != key_coords[" "] else float("inf")
            ver_first = fewest_presses_for_sequence(ver_moves + hor_moves + ["A"], num_presses_map) if (x2, y1) != key_coords[" "] else float("inf")
            new_num_presses_map[(key1, key2)] = min(hor_first, ver_first)
        num_presses_map = new_num_presses_map
    keypad2 = ["789", "456", "123", " 0A"]
    key_coords = {key: (i, j) for i, row in enumerate(keypad2) for j, key in enumerate(row)}
    final_num_presses_map = {}
    for key1, (x1, y1) in key_coords.items():
        for key2, (x2, y2) in key_coords.items():
            ver_moves = ["v" if x2 > x1 else "^"] * abs(x2 - x1)
            hor_moves = [">" if y2 > y1 else "<"] * abs(y2 - y1)
            hor_first = fewest_presses_for_sequence(hor_moves + ver_moves + ["A"], num_presses_map) if (x1, y2) != key_coords[" "] else float("inf")
            ver_first = fewest_presses_for_sequence(ver_moves + hor_moves + ['A'], num_presses_map) if (x2, y1) != key_coords[" "] else float("inf")
            final_num_presses_map[(key1, key2)] = min(hor_first, ver_first)
    
    return final_num_presses_map

def read_input():
    r = []
    with open("inputs/input_21.txt") as f:
        for line in f.readlines():
            r.append(line.strip())
    return r

def part1(codes):
    num_presses_map = get_num_presses_map(2)
    total = 0
    for code in codes:
        num1 = int(code.rstrip("A"))
        l = fewest_presses_for_sequence(code, num_presses_map)
        total += l*num1
    return total

def part2(codes):
    num_presses_map = get_num_presses_map(25)
    total = 0
    for code in codes:
        num1 = int(code.rstrip("A"))
        l = fewest_presses_for_sequence(code, num_presses_map)
        total += l*num1
    return total




if __name__ == "__main__":
    print(f"part 1: {part1(read_input())}")
    print(f"part 2: {part2(read_input())}")

    

