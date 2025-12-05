"""2025 - Day 5 Part 2: Cafeteria"""

from textwrap import dedent

from src.year2025.day05b import solve


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
    assert solve(task) == 14


def test_nested():
    task = dedent(
        """
        1-5
        2-3

        1
        2
        3
        """
    ).strip()
    assert solve(task) == 5
