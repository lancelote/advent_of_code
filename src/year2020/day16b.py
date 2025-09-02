"""2020 - Day 16 Part 2: Ticket Translation."""

from functools import reduce
from operator import mul

from src.year2020.day16a import Puzzle


def solve(task: str) -> int:
    puzzle = Puzzle.from_text(task)
    my_fields = puzzle.get_fields()
    return reduce(mul, (v for k, v in my_fields.items() if k.startswith("departure")))
