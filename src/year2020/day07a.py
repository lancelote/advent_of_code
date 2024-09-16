"""2020 - Day 7 Part 1: Handy Haversacks."""

import re
from collections import defaultdict


def process_data(task: str) -> dict[str, list[str]]:
    parents = defaultdict(list)

    for line in task.strip().split("\n"):
        parent, *children = re.findall(r"\w+\s\w+(?=\sbag)", line)
        for child in children:
            parents[child].append(parent)

    return parents


def solve(task: str) -> int:
    """How many differently colored bags can contain shiny gold?"""
    parents = process_data(task)
    seen = set()
    candidates = parents["shiny gold"]

    while candidates:
        candidate = candidates.pop()
        if candidate not in seen:
            seen.add(candidate)
        candidates.extend(parents[candidate])

    return len(seen)
