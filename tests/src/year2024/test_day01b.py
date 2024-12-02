"""2024 - Day 1 Part 2: Historian Hysteria"""

from textwrap import dedent

from src.year2024.day01b import solve


def test_solve():
    task = dedent(
        """
        3   4
        4   3
        2   5
        1   3
        3   9
        3   3
        """.strip()
    )
    assert solve(task) == 31
