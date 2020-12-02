"""2019 - Day 13 Part 1: Care Package."""
from src.year2019.intcode import Computer


def solve(task: str) -> int:
    """Count the number of blocks."""
    computer = Computer()
    computer.load_program(task)
    computer.execute()
    return list(computer.stdout)[2::3].count(2)
