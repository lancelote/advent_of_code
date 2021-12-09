"""2021 - Day 9 Part 1: Smoke Basin."""
from textwrap import dedent

from src.year2021.day9a import solve


def test_solve():
    task = dedent(
        """
        2199943210
        3987894921
        9856789892
        8767896789
        9899965678
        """.strip()
    )
    assert solve(task) == 15
