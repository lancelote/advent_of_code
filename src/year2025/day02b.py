"""2025 - Day 2 Part 2: Gift Shop"""

import re

from src.year2025.day02a import process_data
from src.year2025.day02a import sum_invalid_ids

PATTERN = re.compile(r"^(\d+)\1+$")


def is_repeated(pk: int) -> bool:
    return PATTERN.match(str(pk)) is not None


def solve(task: str) -> int:
    ranges = process_data(task)
    return sum(sum_invalid_ids(r, is_repeated) for r in ranges)
