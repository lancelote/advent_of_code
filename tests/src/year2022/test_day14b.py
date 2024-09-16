"""2022 - Day 14 Part 2: Regolith Reservoir."""

from textwrap import dedent

from src.year2022.day14b import solve


def test_solve():
    task = dedent(
        """
        498,4 -> 498,6 -> 496,6
        503,4 -> 502,4 -> 502,9 -> 494,9
        """
    ).strip()
    assert solve(task) == 93
