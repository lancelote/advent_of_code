"""2015 - Day 10 Part 1: Elves Look, Elves Say."""

from src.year2015.day10a import iterate


def solve(task: str) -> int:
    state = [int(x) for x in task]
    for _ in range(50):
        state = iterate(state)
    return len(state)
