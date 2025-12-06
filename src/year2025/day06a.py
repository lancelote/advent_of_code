"""2025 - Day 6 Part 1: Trash Compactor"""

from functools import reduce
from operator import mul

type Op = str
type Row = list[int]
type Matrix = list[Row]


def process_data(task: str) -> tuple[Matrix, list[Op]]:
    lines = task.splitlines()
    rows = [[int(x) for x in line.strip().split()] for line in lines[:-1]]
    ops = lines[-1].strip().split()
    return rows, ops


def transpose(matrix: Matrix) -> Matrix:
    n_rows = len(matrix)
    n_cols = len(matrix[0])

    new_matrix: Matrix = []

    for c in range(n_cols):
        new_row: Row = []

        for r in range(n_rows):
            new_row.append(matrix[r][c])

        new_matrix.append(new_row)

    return new_matrix


def solve(task: str) -> int:
    matrix, ops = process_data(task)
    matrix = transpose(matrix)

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
