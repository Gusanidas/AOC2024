from typing import List


def search_ops(left: int, right: List[int], tgt: int, first_part: bool) -> bool:
    if len(right) == 0:
        return left == tgt
    if left > tgt:
        return False
    narg = right.pop()
    if (tgt == 0 or left != 0) and search_ops(left * narg, right[:], tgt, first_part):
        return True
    if search_ops(left + narg, right[:], tgt, first_part):
        return True
    if not first_part and search_ops(
        int(str(left) + str(narg)), right[:], tgt, first_part
    ):
        return True
    return False


def solve():
    with open("inputs/input_day7.txt") as f:
        ops = []
        for line in f.readlines():
            tgt, args = line.strip().split(":")
            tgt, args = tgt.strip(), args.strip()
            args = list(map(int, map(lambda x: x.strip(), args.split(" "))))
            tgt = int(tgt)
            ops.append((tgt, args[::-1]))

    fp, sp = 0, 0
    for tgt, args in ops:
        fp += tgt if search_ops(0, args[:], tgt, True) else 0
        sp += tgt if search_ops(0, args, tgt, False) else 0
    print(f"first_part = {fp}")
    print(f"second = {sp}")


if __name__ == "__main__":
    solve()
