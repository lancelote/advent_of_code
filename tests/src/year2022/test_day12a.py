"""2022 - Day 12 Part 1: Hill Climbing Algorithm."""

from textwrap import dedent

from src.year2022.day12a import solve


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
    assert solve(task) == 31
