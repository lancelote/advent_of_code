"""2020 - Day 3 Part 1: Toboggan Trajectory."""
from typing import List

Plan = List[List[str]]


def process_data(task: str) -> Plan:
    return [list(line) for line in task.strip().split("\n")]


def count_trees(plan: Plan) -> int:
    trees = 0
    x, y = 0, 0
    x_shift, y_shift = 3, 1

    while y < len(plan):
        if plan[y][x] == "#":
            trees += 1

        x = (x + x_shift) % len(plan[0])
        y = y + y_shift

    return trees


def solve(task: str) -> int:
    """Count trees on the way."""
    plan = process_data(task)
    return count_trees(plan)
