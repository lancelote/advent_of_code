"""2022 - Day 4 Part 2: Camp Cleanup."""

from textwrap import dedent

from src.year2022.day04b import solve


def test_solve():
    task = dedent(
        """
        2-4,6-8
        2-3,4-5
        5-7,7-9
        2-8,3-7
        6-6,4-6
        2-6,4-8
        """
    ).strip()
    assert solve(task) == 4
