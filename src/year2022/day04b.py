"""2022 - Day 4 Part 2: Camp Cleanup."""

from src.year2022.day04a import Pair
from src.year2022.day04a import process_data


def overlap(pair: Pair) -> bool:
    (a1, b1), (a2, b2) = pair
    return any(
        [
            a1 <= a2 <= b1,
            a2 <= a1 <= b2,
        ]
    )


def solve(task: str) -> int:
    count = 0

    for pair in process_data(task):
        if overlap(pair):
            count += 1

    return count
