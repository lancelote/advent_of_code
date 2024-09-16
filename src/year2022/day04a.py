"""2022 - Day 4 Part 1: Camp Cleanup."""

from typing import TypeAlias

Section: TypeAlias = tuple[int, int]
Pair: TypeAlias = tuple[Section, Section]


def process_data(task: str) -> list[Pair]:
    pairs = []

    for line in task.splitlines():
        left, right = line.split(",")
        a1, b1 = left.split("-")
        a2, b2 = right.split("-")
        pair = ((int(a1), int(b1)), (int(a2), int(b2)))
        pairs.append(pair)

    return pairs


def contain(pair: Pair) -> bool:
    (a1, b1), (a2, b2) = pair
    return (a1 >= a2 and b1 <= b2) or (a1 <= a2 and b1 >= b2)


def solve(task: str) -> int:
    count = 0

    for pair in process_data(task):
        if contain(pair):
            count += 1

    return count
