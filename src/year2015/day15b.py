"""2015 - Day 15 Part 2: Science for Hungry People."""

from src.year2015.day15a import solve as solve_part1


def solve(task: str) -> int:
    return solve_part1(task, limit_calories=True)
