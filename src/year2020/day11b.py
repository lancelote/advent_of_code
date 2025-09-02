"""2020 - Day 11 Part 2: Seating System."""

from src.year2020.day11a import SHIFTS
from src.year2020.day11a import Cell
from src.year2020.day11a import Matrix
from src.year2020.day11a import count_occupied


def count_visible(i: int, j: int, matrix: Matrix) -> int:
    """Count visible occupied seats from the given one."""
    visible = 0

    for shift_i, shift_j in SHIFTS:
        new_i = i + shift_i
        new_j = j + shift_j

        while matrix.is_inside(new_i, new_j):
            if matrix[new_i][new_j] is Cell.OCCUPIED:
                visible += 1
                break
            elif matrix[new_i][new_j] is Cell.EMPTY:
                break
            else:
                new_i += shift_i
                new_j += shift_j

    return visible


def solve(task: str) -> int:
    """How many seats are occupied?"""
    return count_occupied(task, count_visible, count_limit=5)
