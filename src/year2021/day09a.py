"""2021 - Day 9 Part 1: Smoke Basin."""

from collections.abc import Iterator
from typing import NamedTuple

Heightmap = list[list[int]]

SHIFTS = [
    (-1, 0),
    (0, +1),
    (+1, 0),
    (0, -1),
]


class Point(NamedTuple):
    i: int
    j: int
    height: int


def adjacent(point: Point, heightmap: Heightmap) -> Iterator[Point]:
    """Yields given point neighbors."""
    row_length = len(heightmap[0])
    col_length = len(heightmap)

    for di, dj in SHIFTS:
        new_i = point.i + di
        new_j = point.j + dj
        valid_i = 0 <= new_i < col_length
        valid_j = 0 <= new_j < row_length

        if valid_i and valid_j:
            height = heightmap[new_i][new_j]
            yield Point(new_i, new_j, height)


def lowest(heightmap: Heightmap) -> Iterator[Point]:
    """Yields the lowest points on the heightmap."""
    for i, row in enumerate(heightmap):
        for j, height in enumerate(row):
            current = Point(i, j, height)
            if all(
                neighbor.height > current.height
                for neighbor in adjacent(current, heightmap)
            ):
                yield current


def risk_level(point: int) -> int:
    return point + 1


def solve(task: str) -> int:
    """Sum risk level of the lowest heightmap points."""
    heightmap = [
        [int(x) for x in list(line.strip())] for line in task.strip().split("\n")
    ]
    low_points = lowest(heightmap)
    return sum(risk_level(point.height) for point in low_points)
