"""2020 - Day 14 Part 2: Docking Data."""
from textwrap import dedent

from src.year2020.day14b import solve


def test_solve():
    task = dedent(
        """
            mask = 000000000000000000000000000000X1001X
            mem[42] = 100
            mask = 00000000000000000000000000000000X0XX
            mem[26] = 1
        """
    )
    assert solve(task) == 208
