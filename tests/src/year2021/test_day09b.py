"""2021 - Day 9 Part 2: Smoke Basin."""

from textwrap import dedent

from src.year2021.day09b import solve


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
    assert solve(task) == 1134
