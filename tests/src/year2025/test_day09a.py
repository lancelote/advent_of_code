"""2025 - Day 9 Part 1: Playground"""

from textwrap import dedent

from src.year2025.day09a import solve


def test_solve():
    task = dedent(
        """
        7,1
        11,1
        11,7
        9,7
        9,5
        2,5
        2,3
        7,3
        """
    ).strip()
    assert solve(task) == 50
