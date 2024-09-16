"""2016 - Day 3 Part 2: Squares With Three Sides."""

from itertools import chain

from src.year2016.day03a import count_possible


def process_data(data: str) -> list[tuple[int, int, int]]:
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
