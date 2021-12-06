"""2021 - Day 6 Part 1: Lanternfish."""
from textwrap import dedent

from src.year2021.day6a import solve


def test_solve():
    task = dedent(
        """
        3,4,3,1,2
        """.strip()
    )
    assert solve(task) == 5934
