"""2019 - Day 5 Part 1: Sunny with a Chance of Asteroids."""
from src.year2019.intcode import Computer


def solve(task: str) -> int:
    """Run diagnostic command."""
    computer = Computer()
    computer.load_program(task)
    computer.stdin.append(1)

    computer.execute()

    return computer.stdout.pop()
