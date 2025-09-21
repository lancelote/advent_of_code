"""2024 - Day 1 Part 1: Historian Hysteria"""


def solve(task: str) -> int:
    left: list[int] = []
    right: list[int] = []

    for line in task.split("\n"):
        a, b = line.split()
        left.append(int(a))
        right.append(int(b))

    left.sort()
    right.sort()

    return sum(abs(x - y) for x, y in zip(left, right, strict=True))
