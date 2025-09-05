"""2020 - Day 11 Part 1: Seating System."""

from __future__ import annotations

from collections.abc import Callable
from collections.abc import Iterator
from dataclasses import dataclass
from enum import Enum
from typing import assert_never

SHIFTS = [
    # i   j
    (-1, -1),  # top left
    (-1, +0),  # top
    (-1, +1),  # top right
    (+0, +1),  # right
    (+1, +1),  # bottom right
    (+1, +0),  # bottom
    (+1, -1),  # bottom left
    (+0, -1),  # left
]


class Cell(Enum):
    EMPTY = "L"
    FLOOR = "."
    OCCUPIED = "#"


def generate_new(cell: Cell, occupied: int, limit: int) -> Cell:
    match cell:
        case Cell.FLOOR:
            return Cell.FLOOR

        case Cell.EMPTY:
            return Cell.OCCUPIED if occupied == 0 else Cell.EMPTY

        case Cell.OCCUPIED:
            return Cell.EMPTY if occupied >= limit else Cell.OCCUPIED

        case _:
            assert_never(cell)


@dataclass
class Matrix:
    data: list[list[Cell]]

    @classmethod
    def from_task(cls, task: str) -> Matrix:
        data = [
            [Cell(char) for char in list(line)] for line in task.strip().split("\n")
        ]
        return cls(data)

    @property
    def occupied(self) -> int:
        return sum(line.count(Cell.OCCUPIED) for line in self.data)

    def is_inside(self, i: int, j: int) -> bool:
        """Are the given indexes i and j inside the matrix range?"""
        i_in_range = 0 <= i < len(self.data)
        j_in_range = 0 <= j < len(self.data[0])
        return i_in_range and j_in_range

    def __getitem__(self, i: int) -> list[Cell]:
        return self.data[i]

    def __len__(self) -> int:
        return len(self.data)

    def __iter__(self) -> Iterator[list[Cell]]:
        return iter(self.data)


type Rule = Callable[[int, int, Matrix], int]


def count_adjacent(i: int, j: int, matrix: Matrix) -> int:
    """Count occupied adjacent neighbors."""
    adjacent = 0

    for shift_i, shift_j in SHIFTS:
        new_i = i + shift_i
        new_j = j + shift_j

        i_in_range = 0 <= new_i < len(matrix)
        j_in_range = 0 <= new_j < len(matrix[0])

        if i_in_range and j_in_range:
            if matrix[new_i][new_j] is Cell.OCCUPIED:
                adjacent += 1

    return adjacent


def generate_next(matrix: Matrix, limit: int, count_rule: Rule) -> Matrix:
    """Generate new matrix generation from the given one applying the rule."""
    next_data: list[list[Cell]] = []

    for i, line in enumerate(matrix):
        new_line: list[Cell] = []
        for j, cell in enumerate(line):
            occupied = count_rule(i, j, matrix)
            new_line.append(generate_new(cell, occupied, limit))
        next_data.append(new_line)

    return Matrix(next_data)


def count_occupied(task: str, count_rule: Rule, count_limit: int) -> int:
    """Count occupied seats once matrix generation is stabilized."""
    current_matrix = Matrix.from_task(task)

    while True:
        next_matrix = generate_next(current_matrix, count_limit, count_rule)
        if current_matrix == next_matrix:
            break
        current_matrix = next_matrix

    return current_matrix.occupied


def solve(task: str) -> int:
    """How many seats are occupied?"""
    return count_occupied(task, count_adjacent, count_limit=4)
