"""2019 - Day 9 Part 1: Sensor Boost."""

from src.year2019.intcode import Computer


def solve(task: str) -> int:
    """Find BOOST key code."""
    computer = Computer()
    computer.load_program(task)
    computer.stdin.append(1)  # test mode
    computer.execute()
    return computer.stdout.pop()
