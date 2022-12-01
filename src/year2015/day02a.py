"""2015 - Day 2 Part 1: I Was Told There Would Be No Math."""
from collections import namedtuple

Box = namedtuple("Box", ["length", "height", "width"])


def process_data(data: str) -> list[Box]:
    r"""Process string data to convenient list of tuples.

    Args:
        data (str): length x width x height \n ... (without spaces)

    Returns:
        list: list of tuples [(length, width, height), (...), ...]
    """
    dimensions = [
        Box(*[int(x) for x in size.split("x")])
        for size in data.strip().split("\n")
    ]
    return dimensions


def solve(task: str) -> int:
    r"""Solve the puzzle.

    Args:
        task (str): length x width x height \n ... (without spaces)

    Returns:
        int: Total square feet of wrapping paper
    """
    result = 0
    data = process_data(task)
    for size in data:
        sides = (
            size.length * size.height,
            size.length * size.width,
            size.height * size.width,
        )
        result += 2 * sum(sides) + min(sides)
    return result
