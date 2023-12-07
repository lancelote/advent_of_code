"""2023 - Day 6 Part 1: Wait For It"""
from textwrap import dedent

from src.year2023.day06a import solve


def test_solve():
    task = dedent(
        """
        Time:      7  15   30
        Distance:  9  40  200
        """
    ).strip()
    assert solve(task) == 288
