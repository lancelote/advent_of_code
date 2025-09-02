"""2020 - Day 7 Part 2: Handy Haversacks."""

from __future__ import annotations

import re
from collections import defaultdict
from typing import NamedTuple, TypeAlias


class InnerBag(NamedTuple):
    num: int
    color: str

    @classmethod
    def from_text(cls, text: str) -> InnerBag:
        """From '2 clear indigo'."""
        match = re.match(r"(\d+) (.+)", text)
        if match:
            count, name = match.groups()
        else:
            raise ValueError(f"unexpected child: {text}")
        return cls(int(count), name)


Bags: TypeAlias = dict[str, list[InnerBag]]


def process_data(task: str) -> Bags:
    bags = defaultdict(list)

    for line in task.strip().split("\n"):
        parent, *children = re.findall(r"(^\w+ \w+|\d+ \w+ \w+(?= bag))", line)
        bags[parent] = [InnerBag.from_text(child) for child in children]

    return bags


def count_bags(bags: Bags, parent: str = "shiny gold") -> int:
    return sum(
        child.num + child.num * count_bags(bags, child.color)
        for child in bags[parent]
    )


def solve(task: str) -> int:
    """How many bags must be in shiny gold?"""
    bags = process_data(task)
    return count_bags(bags)
