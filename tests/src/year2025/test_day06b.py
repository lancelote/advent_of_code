"""2025 - Day 6 Part 2: Trash Compactor"""

from textwrap import dedent

from src.year2025.day06b import solve


def test_solve():
    task = dedent(
        r"""
        123 328  51 64 
         45 64  387 23 
          6 98  215 314
        *   +   *   +  
        """  # noqa: W291
    ).strip()
    assert solve(task) == 3263827
