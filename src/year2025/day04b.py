"""2025 - Day 4 Part 2: Printing Department"""

from src.year2025.day04a import can_be_removed
from src.year2025.day04a import process_data


def remove_accessible(diagram: list[list[str]]) -> int:
    count = 0

    n_rows = len(diagram)
    n_cols = len(diagram)

    for r in range(n_rows):
        for c in range(n_cols):
            if can_be_removed(r, c, diagram):
                diagram[r][c] = "."
                count += 1

    return count


def solve(task: str) -> int:
    total_removed = 0
    diagram = process_data(task)

    while (removed := remove_accessible(diagram)) != 0:
        total_removed += removed

    return total_removed
