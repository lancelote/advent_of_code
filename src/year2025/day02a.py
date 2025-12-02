"""2025 - Day 2 Part 1: Gift Shop"""

from dataclasses import dataclass
from typing import Callable


@dataclass
class Range:
    left: int
    right: int

    @classmethod
    def from_str(cls, txt: str) -> Range:
        left, right = txt.split("-")
        return Range(int(left), int(right))


def process_data(task: str) -> list[Range]:
    return [Range.from_str(part) for part in task.split(",")]


def is_left_equals_right(pk: int) -> bool:
    txt = str(pk)

    if len(txt) % 2 != 0:
        return False

    m = len(txt) // 2
    return txt[:m] == txt[m:]


def sum_invalid_ids(r: Range, is_invalid: Callable[[int], bool]) -> int:
    total = 0

    for x in range(r.left, r.right + 1):
        if is_invalid(x):
            total += x

    return total


def solve(task: str) -> int:
    ranges = process_data(task)
    return sum(sum_invalid_ids(r, is_left_equals_right) for r in ranges)
