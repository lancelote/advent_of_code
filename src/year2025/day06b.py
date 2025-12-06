"""2025 - Day 6 Part 2: Trash Compactor"""

from functools import reduce
from operator import mul

type Op = str
type Row = list[int]
type Matrix = list[Row]


def transpose(lines: list[str]) -> str:
    n_rows = len(lines)
    n_cols = len(lines[0])

    new_data: list[list[str]] = []

    for c in range(n_cols - 1, -1, -1):
        new_row: list[str] = []

        for r in range(n_rows):
            new_row.append(lines[r][c])

        new_data.append(new_row)

    return "\n".join("".join(line).strip() for line in new_data)


def process_data(task: str) -> tuple[Matrix, list[Op]]:
    lines = task.splitlines()
    ops = lines[-1].strip().split()[::-1]
    numbers_part = transpose(lines[:-1])

    matrix: Matrix = []

    for block in numbers_part.split("\n\n"):
        matrix.append([int(line) for line in block.splitlines()])

    return matrix, ops


def solve(task: str) -> int:
    matrix, ops = process_data(task)

    total = 0

    for i, row in enumerate(matrix):
        op = ops[i]

        if op == "+":
            total += sum(row)
        elif op == "*":
            total += reduce(mul, row)
        else:
            raise ValueError(f"unknown operator {op}")

    return total
