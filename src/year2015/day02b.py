"""2015 - Day 2 Part 2: I Was Told There Would Be No Math."""
from functools import reduce
from operator import mul

from src.year2015.day02a import process_data


def solve(task: str) -> int:
    r"""Solve the puzzle.

    Args:
        task (str): length x width x height \n ... (without spaces)

    Returns:
        int: Total feet of ribbon

    """
    data = process_data(task)
    return sum(
        2 * (sum(size) - max(size)) + reduce(mul, size, 1) for size in data
    )
