"""2016 - Day 3 Part 1: Squares With Three Sides.

Now that you can think clearly, you move deeper into the labyrinth of hallways
and office furniture that makes up this part of Easter Bunny HQ. This must be
a graphic design department; the walls are covered in specifications for
triangles.

Or are they?

The design document gives the side lengths of each triangle it describes,
but... 5 10 25? Some of these aren't triangles. You can't help but mark the
impossible ones.

In a valid triangle, the sum of any two sides must be larger than the remaining
side. For example, the "triangle" given above is impossible, because 5 + 10 is
not larger than 25.

In your puzzle input, how many of the listed triangles are possible?
"""
from typing import List
from typing import Tuple


def process_data(data: str) -> List[Tuple[int, int, int]]:
    """Parse the raw data.

    Convert raw triangle data:

        1 2 3
        4 5 6

    Into list of tuples, where each item is a triangle with a, b, c sides
    """
    triangles = []
    for triangle in data.strip().split("\n"):
        a, b, c = triangle.split()
        triangles.append((int(a), int(b), int(c)))
    return triangles


def is_bad(triangle: Tuple[int, int, int]) -> bool:
    """Check if there can exist such triangle."""
    longest = max(triangle)
    return sum(triangle) - longest <= longest


def count_possible(triangles: List[Tuple[int, int, int]]) -> int:
    """Calculate the number of possible triangles."""
    possible = 0
    for triangle in triangles:
        if not is_bad(triangle):
            possible += 1
    return possible


def solve(task: str) -> int:
    """Solve the puzzle."""
    triangles = process_data(task)
    return count_possible(triangles)
