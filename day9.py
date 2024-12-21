from collections import deque
from os import register_at_fork
import re
from typing import List, Tuple


def expand_drive(drive: str) -> List[str]:
    expanded_drive = []
    for i, let in enumerate(drive):
        if i % 2 == 0:
            expanded_drive += int(let) * [str(i // 2)]
        else:
            expanded_drive += ["."] * int(let)

    return expanded_drive


def rearrange_drive(drive: List[str]) -> List[int]:
    q = deque(drive)
    compressed_drive = []
    while q:
        disk = q.popleft()
        if disk == ".":
            while q and q[-1] == ".":
                q.pop()
            if q:
                compressed_drive.append(int(q.pop()))
        else:
            compressed_drive.append(int(disk))

    return compressed_drive


def get_checksum(drive: List[int]) -> int:
    return sum([i * x for i, x in enumerate(drive)])


def part_one():
    with open("inputs/input_day_9.txt") as f:
        drive = f.read().strip()
        drive = expand_drive(drive)
        drive = rearrange_drive(drive)
        checksum = get_checksum(drive)
    print(f"part one = {checksum}")


def expand_drive_2(drive: str) -> List[Tuple[str, int]]:
    expanded_drive = []
    for i, let in enumerate(drive):
        if i % 2 == 0:
            expanded_drive.append((str(i // 2), int(let)))
        else:
            expanded_drive.append((".", int(let)))

    return expanded_drive


def rearrange_drive_2(drive):
    idx = len(drive) - 1
    while idx > 0:
        if drive[idx][0] == ".":
            idx -= 1
            continue
        id, length = drive[idx]
        for i in range(idx):
            oid, olength = drive[i]
            if oid == "." and olength > length:
                drive[i] = (".", olength - length)
                drive.insert(i, (id, length))
                idx += 1
                drive[idx] = (".", length)
                break
            elif oid == "." and olength == length:
                drive[i] = (id, length)
                drive[idx] = (".", length)
                break
        idx -= 1
    r = []
    for id, length in drive:
        r += [0 if id == "." else int(id)] * length
    return r


def part_two():
    with open("inputs/input_day_9.txt") as f:
        drive = f.read().strip()
        drive = expand_drive_2(drive)
        drive = rearrange_drive_2(drive)
        checksum = get_checksum(drive)
    print(f"part tw0 = {checksum}")


if __name__ == "__main__":
    part_one()
    part_two()
