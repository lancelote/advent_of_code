"""2025 - Day 5 Part 1: Cafeteria"""

from textwrap import dedent

from src.year2025.day05a import solve


def test_solve():
    task = dedent(
        """
        3-5
        10-14
        16-20
        12-18

        1
        5
        8
        11
        17
        32
        """
    ).strip()
    assert solve(task) == 3
