"""2023 - Day 12 Part 2: Hot Springs"""
from src.year2023.day12a import Field


def solve(task: str) -> int:
    field = Field.from_task(task, fold=True)
    return sum(r.arrangements for r in field.rows)
