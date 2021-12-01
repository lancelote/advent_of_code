"""2021 - Day 1 Part 1: Sonar Sweep."""
from itertools import pairwise


def solve(task: str) -> int:
    depths = (int(x) for x in task.strip().split("\n"))
    return sum(a < b for (a, b) in pairwise(depths))
