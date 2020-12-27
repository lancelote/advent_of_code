"""2020 - Day 11 Part 1: Seating System."""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import List

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

    def generate_new(self, adjacent: int) -> Cell:
        if self is Cell.FLOOR:
            return Cell.FLOOR
        elif self is Cell.EMPTY:
            return Cell.OCCUPIED if adjacent == 0 else Cell.EMPTY
        elif self is Cell.OCCUPIED:
            return Cell.EMPTY if adjacent >= 4 else Cell.OCCUPIED
        else:
            raise ValueError(f"unexpected cell type: {self}")


@dataclass
class Matrix:
    data: List[List[Cell]]

    @classmethod
    def from_task(cls, task: str) -> Matrix:
        data = [
            [Cell(char) for char in list(line)]
            for line in task.strip().split("\n")
        ]
        return cls(data)

    @property
    def occupied(self) -> int:
        return sum(line.count(Cell.OCCUPIED) for line in self.data)

    def count_adjacent(self, i: int, j: int) -> int:
        adjacent = 0

        for (shift_i, shift_j) in SHIFTS:
            new_i = i + shift_i
            new_j = j + shift_j

            i_in_range = 0 <= new_i < len(self.data)
            j_in_range = 0 <= new_j < len(self.data[0])

            if i_in_range and j_in_range:
                if self.data[new_i][new_j] is Cell.OCCUPIED:
                    adjacent += 1

        return adjacent

    def generate_new(self) -> Matrix:
        new_data = []

        for i, line in enumerate(self.data):
            new_line = []
            for j, cell in enumerate(line):
                adjacent = self.count_adjacent(i, j)
                new_line.append(cell.generate_new(adjacent))
            new_data.append(new_line)

        return Matrix(new_data)


def solve(task: str) -> int:
    """How many seats are empty?"""
    current_matrix = Matrix.from_task(task)

    while True:
        next_matrix = current_matrix.generate_new()
        if current_matrix == next_matrix:
            break
        current_matrix = next_matrix

    return current_matrix.occupied
