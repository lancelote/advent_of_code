"""2019 - Day 9 Part 2: Sensor Boost."""

from src.year2019.intcode import Computer


def solve(task: str) -> int:
    """Find coordinates of the distress signal."""
    computer = Computer()
    computer.load_program(task)
    computer.stdin.append(2)  # boost
    computer.execute()
    return computer.stdout.pop()
