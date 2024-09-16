"""2019 - Day 2 Part 2: 1202 Program Alarm."""

from src.year2019.intcode import Computer


def solve(task: str) -> int:
    """Find out which noun and verb results in 19690720 output."""
    for i in range(100):
        for j in range(100):
            computer = Computer()
            computer.load_program(task)
            computer.set_noun_and_verb(i, j)
            computer.execute()
            if computer.output == 19690720:
                return 100 * computer.noun + computer.verb

    return -1
