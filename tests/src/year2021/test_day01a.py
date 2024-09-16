"""2021 - Day 1 Part 1: Sonar Sweep."""

from textwrap import dedent

from src.year2021.day01a import solve


def test_solve():
    task = dedent(
        """
        199
        200
        208
        210
        200
        207
        240
        269
        260
        263
        """.strip()
    )
    assert solve(task) == 7
