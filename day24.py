from collections import deque
from typing import Dict

def parse_initial_value(line: str, cells: Dict[str, int]) -> None:
    cell_name, value = [x.strip() for x in line.split(":")]
    cells[cell_name] = bool(int(value))
    #print(f"cell {cell_name} = {cells[cell_name]}")


def parse_logic_line(line: str):
    operation, result = line.split('->')
    operation = operation.strip().split(" ")
    arg1, op, arg2 = [x.strip() for x in operation]
    return (arg1, arg2), op, result.strip()

def apply_logic(cells: Dict[str, int], arg1: str, arg2: str, op: str, result: str) -> None:
    if op == 'AND':
        cells[result] = cells[arg1] & cells[arg2]
    elif op == 'OR':
        cells[result] = cells[arg1] | cells[arg2]
    elif op == 'XOR':
        cells[result] = cells[arg1] ^ cells[arg2]
    else:
        print(f"Unknown operation: {op}")

def sort_logic_ops(logic_ops, cells):
    seen, q = set(cells.keys()), deque(logic_ops)
    while q:
        args, op, result = q.popleft()
        if args[0] in seen and args[1] in seen:
            apply_logic(cells, *args, op, result)
            seen.add(result)
        else:
            q.append((args, op, result))
    


def part1():
    with open('inputs/input_24.txt') as f:
        lines = f.readlines()
        cells = {}
        op_lines = []
        for line in lines:
            if len(line.strip()) == 0:
                continue
            if '->' in line:
                op_lines.append(parse_logic_line(line))
            else:
                parse_initial_value(line, cells)

        sort_logic_ops(op_lines, cells)

        zbits = sorted([(n,v) for n,v in cells.items() if n.startswith("z")], reverse=True)
        zbits = ''.join([str(int(v)) for n,v in zbits])
        z_int_value = int(zbits, 2)
        print(f"Part 1: {z_int_value}")


if __name__ == '__main__':
    part1()