"""2024 - Day 2 Part 1: Red-Nosed Reports"""

from textwrap import dedent

from src.year2024.day02a import solve


def test_solve():
    task = dedent(
        """
        7 6 4 2 1
        1 2 7 8 9
        9 7 6 2 1
        1 3 2 4 5
        8 6 4 4 1
        1 3 6 7 9
        """.strip()
    )
    assert solve(task) == 2
