"""2019 - Day 5 Part 1: Sunny with a Chance of Asteroids."""

from src.utils.cli import capture
from src.year2019.intcode import Computer


def solve(task: str) -> int:
    """Run diagnostic command."""
    computer = Computer()
    computer.load_program(task)

    with capture('1') as out:
        computer.execute()

    return int(out.getvalue().split('\n')[-2])
