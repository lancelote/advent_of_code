"""2020 - Day 6 Part 2: Custom Customs."""
from functools import reduce
from typing import List
from typing import Set


def process_data(task: str) -> List[List[Set[str]]]:
    return [
        [set(user) for user in group.split("\n")]
        for group in task.strip().split("\n\n")
    ]


def solve(task: str) -> int:
    """Count the sum of answers which everyone gave per group."""
    groups = process_data(task)
    return sum(
        len(reduce(lambda x, y: x.intersection(y), group)) for group in groups
    )
