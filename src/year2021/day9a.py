"""2021 - Day 9 Part 1: Smoke Basin."""
from typing import Iterator

SHIFTS = [
    (-1, 0),
    (0, +1),
    (+1, 0),
    (0, -1),
]


def adjacent(i: int, j: int, points: list[list[int]]) -> Iterator[int]:
    row_length = len(points[0])
    col_length = len(points)

    for di, dj in SHIFTS:
        valid_i = 0 <= i + di < col_length
        valid_j = 0 <= j + dj < row_length

        if valid_i and valid_j:
            yield points[i + di][j + dj]


def lowest(points: list[list[int]]) -> list[int]:
    result = []

    for i, row in enumerate(points):
        for j, item in enumerate(row):
            for neighbor in adjacent(i, j, points):
                if neighbor <= item:
                    break
            else:
                result.append(item)

    return result


def risk_level(point: int) -> int:
    return point + 1


def solve(task: str) -> int:
    points = [
        [int(x) for x in list(line.strip())]
        for line in task.strip().split("\n")
    ]
    low_points = lowest(points)
    return sum(risk_level(point) for point in low_points)
