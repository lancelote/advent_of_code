"""2021 - Day 14 Part 1: Extended Polymerization."""

from collections import Counter
from itertools import pairwise
from typing import TypeAlias

Polymer: TypeAlias = list[str]
Insertions: TypeAlias = dict[tuple[str, ...], str]


def parse_task(task: str) -> tuple[Polymer, Insertions]:
    raw_polymer, raw_insertions = task.split("\n\n")
    polymer = list(raw_polymer)
    insertions = {}

    for insertion in raw_insertions.splitlines():
        base, output = insertion.split(" -> ")
        insertions[tuple(base)] = output

    return polymer, insertions


def step(polymer: Polymer, insertions: Insertions) -> Polymer:
    new_polymer = [polymer[0]]

    for a, b in pairwise(polymer):
        new_polymer.append(insertions[(a, b)])
        new_polymer.append(b)

    return new_polymer


def solve(task: str) -> int:
    polymer, insertions = parse_task(task)

    for _ in range(10):
        polymer = step(polymer, insertions)

    [(_, most_common), *_, (_, least_common)] = Counter(polymer).most_common()
    return most_common - least_common
