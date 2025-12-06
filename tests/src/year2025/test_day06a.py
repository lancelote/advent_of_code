"""2025 - Day 6 Part 1: Trash Compactor"""

from textwrap import dedent

from src.year2025.day06a import solve


def test_solve():
    task = dedent(
        """
        123 328  51 64
         45 64  387 23
          6 98  215 314
        *   +   *   +
        """
    ).strip()
    assert solve(task) == 4277556
