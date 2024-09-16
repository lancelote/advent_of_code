"""2019 - Day 2 Part 1: 1202 Program Alarm."""

from src.year2019.intcode import Computer


def solve(task: str) -> int:
    """Execute a program and return 0 index opcode."""
    computer = Computer()
    computer.load_program(task)
    computer.set_noun_and_verb(12, 2)

    computer.execute()

    return computer.output
