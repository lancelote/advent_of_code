"""2015 - Day 3 Part 1: Perfectly Spherical Houses in a Vacuum."""
from collections import defaultdict
from collections import namedtuple

Coordinates = namedtuple("Coordinates", ["x", "y"])
SHIFT = {
    "<": Coordinates(-1, 0),
    "^": Coordinates(0, 1),
    ">": Coordinates(1, 0),
    "v": Coordinates(0, -1),
}


def visit_houses(task: str) -> dict[Coordinates, int]:
    """Deliver presents.

    Args:
        task (str): '>^<v...'

    Returns:
        dct: {position: number_of_presents, ...}

    """
    current_position = Coordinates(0, 0)
    visited_houses = defaultdict(int)
    visited_houses[current_position] = 1

    for direction in task:
        current_position = Coordinates(
            current_position.x - SHIFT[direction].x,
            current_position.y - SHIFT[direction].y,
        )
        visited_houses[current_position] += 1
    return visited_houses


def solve(task: str) -> int:
    """Solve the puzzle.

    Args:
        task (str): '>^<v...'

    Returns:
        int: Number of houses with at least one present

    """
    visited_houses = visit_houses(task)
    return len(visited_houses)
