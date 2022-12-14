"""2022 - Day 12 Part 2: Hill Climbing Algorithm."""
from textwrap import dedent

from src.year2022.day12b import solve


def test_solve():
    task = dedent(
        """
        Sabqponm
        abcryxxl
        accszExk
        acctuvwj
        abdefghi
        """
    ).strip()
    assert solve(task) == 29
