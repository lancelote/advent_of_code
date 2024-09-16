"""2018 - Day 6 Part 2: Chronal Coordinates tests."""

from textwrap import dedent

from src.year2018.day06b import solve


def test_solve():
    sample_task = dedent(
        """
        1, 1
        1, 6
        8, 3
        3, 4
        5, 5
        8, 9
    """
    )
    assert solve(sample_task, limit=32) == 16
