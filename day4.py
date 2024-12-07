from typing import List


def search_word(input_letters: List[List[str]], word: str):
    total = 0
    directions_x = [
        (0, 0, len(input_letters)),
        (1, 0, len(input_letters) - len(word) + 1),
        (-1, len(word) - 1, len(input_letters)),
    ]
    directions_y = [
        (0, 0, len(input_letters[0])),
        (1, 0, len(input_letters[0]) - len(word) + 1),
        (-1, len(word) - 1, len(input_letters[0])),
    ]

    for i, row in enumerate(input_letters):
        for j, let in enumerate(row):
            for dx, cond1x, cond2x in directions_x:
                for dy, cond1y, cond2y in directions_y:
                    if dx == 0 and dy == 0:
                        continue
                    if cond1x <= i < cond2x and cond1y <= j < cond2y:
                        cx, cy, tn = i, j, 0
                        while tn < len(word) and input_letters[cx][cy] == word[tn]:
                            tn += 1
                            cx += dx
                            cy += dy
                        if tn == len(word):
                            total += 1
    return total


def search_xmas(input_letters: List[List[str]]):
    total = 0

    for i, row in enumerate(input_letters):
        for j, let in enumerate(row):
            if (
                1 <= i < len(input_letters) - 1
                and 0 < j < len(input_letters) - 1
                and let == "A"
            ):
                first_stick, second_stick = False, False
                valid = [("M", "S"), ("S", "M")]
                if (input_letters[i - 1][j - 1], input_letters[i + 1][j + 1]) in valid:
                    first_stick = True
                if (
                    first_stick
                    and (input_letters[i - 1][j + 1], input_letters[i + 1][j - 1])
                    in valid
                ):
                    second_stick = True
                total += second_stick
    return total


def solve():
    with open("inputs/input_day4.txt", "r") as f:
        input_letters = []
        for line in f.readlines():
            input_letters.append(list(line))
        first_part = search_word(input_letters, "XMAS")
        second_part = search_xmas(input_letters)
    return first_part, second_part


if __name__ == "__main__":
    first_part, second_part = solve()
    print(f"First part = {first_part}")
    print(f"Second part = {second_part}")
