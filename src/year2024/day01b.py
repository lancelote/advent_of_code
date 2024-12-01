"""2024 - Day 1 Part 2:"""

from collections import defaultdict


def solve(task: str) -> int:
    left: list[int] = []
    right: dict[int, int] = defaultdict(int)

    lines = task.split("\n")
    for line in lines:
        a, b = line.split()
        left.append(int(a))
        right[int(b)] += 1

    return sum(x * right[x] for x in left)
