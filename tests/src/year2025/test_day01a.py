"""2025 - Day 1 Part 1: Secret Entrance"""

from textwrap import dedent

from src.year2025.day01a import solve


def test_solve():
    task = dedent(
        """
        L68
        L30
        R48
        L5
        R60
        L55
        L1
        L99
        R14
        L82
        """
    ).strip()
    assert solve(task) == 3
