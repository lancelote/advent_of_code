"""2020 - Day 14 Part 1: Docking Data."""
from textwrap import dedent

from src.year2020.day14a import solve


def test_solve():
    task = dedent(
        """
            mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
            mem[8] = 11
            mem[7] = 101
            mem[8] = 0
        """
    )
    assert solve(task) == 165
