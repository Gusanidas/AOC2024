import re

def get_mul_total(text):
    pattern = r"mul\((\d{1,3},\d{1,3})\)"
    matches = re.findall(pattern, text)
    total = 0
    for match in matches:
        x, y = map(int, match.split(','))
        total += x*y
    return total

def part_one():
    with open('inputs/input_day3a.txt') as f:
        text = f.read()
        total = get_mul_total(text)
        print(f"Part 1: {total}")

def part_two():
    with open('inputs/input_day3a.txt') as f:
        text = f.read()
        new_text, copy = "", True
        for i, let in enumerate(text):
            if i<len(text)-7 and text[i:i+4] == "do()":
                copy = True
            if i<len(text)-7 and text[i:i+7] == "don't()":
                copy = False
            if copy:
                new_text += let

        total = get_mul_total(new_text)
        print(f"Part 2: {total}")


if __name__ == '__main__':
    part_one()
    part_two()