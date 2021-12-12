"""2016 - Day 3 Part 2: Squares With Three Sides.

Now that you've helpfully marked up their design documents, it occurs to you
that triangles are specified in groups of three vertically. Each set of three
numbers in a column specifies a triangle. Rows are unrelated.

For example, given the following specification, numbers with the same hundreds
digit would be part of the same triangle:

    101 301 501
    102 302 502
    103 303 503
    201 401 601
    202 402 602
    203 403 603

In your puzzle input, and instead reading by columns, how many of the listed
triangles are possible?
"""
from itertools import chain
from typing import List
from typing import Tuple

from src.year2016.day03a import count_possible


def process_data(data: str) -> List[Tuple[int, int, int]]:
    """Parse the raw data.

    Convert raw triangle data:

        1 4 7
        2 5 8
        3 6 9

    Into list of tuples, where each item is a triangle with a, b, c sides
    Note that triangle sides are given in the columns and not in rows
    """
    triangles = []
    rows = [row.split() for row in data.strip().split("\n")]
    sides = list(map(int, chain.from_iterable(zip(*rows))))

    for i in range(0, len(sides), 3):
        a, b, c = sides[i : i + 3]
        triangles.append((a, b, c))
    return triangles


def solve(task: str) -> int:
    """Solve the puzzle."""
    triangles = process_data(task)
    return count_possible(triangles)
