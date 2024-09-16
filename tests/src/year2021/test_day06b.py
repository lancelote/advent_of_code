"""2021 - Day 6 Part 2: Lanternfish."""

from textwrap import dedent

from src.year2021.day06b import solve


def test_solve():
    task = dedent(
        """
        3,4,3,1,2
        """.strip()
    )
    assert solve(task) == 26984457539
