"""2020 - Day 6 Part 1: Custom Customs."""
from typing import List
from typing import Set


def process_data(task: str) -> List[Set[str]]:
    return [
        set(group.replace("\n", "")) for group in task.strip().split("\n\n")
    ]


def solve(task: str) -> int:
    """Count sum of unique answers per group."""
    groups = process_data(task)
    return sum(len(group) for group in groups)
