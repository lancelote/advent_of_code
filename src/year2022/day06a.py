"""2022 - Day 6 Part 1: Tuning Trouble."""


def find_unique(data: str, n: int) -> int:
    start = 0
    last: set[str] = set()

    for i, x in enumerate(data, start=1):
        while x in last:
            last.remove(data[start])
            start += 1
        last.add(x)
        if len(last) == n:
            return i

    raise ValueError("no 4 unique found")


def solve(task: str) -> int:
    return find_unique(task, 4)
