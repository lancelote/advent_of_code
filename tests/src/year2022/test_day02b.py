"""2022 - Day 2 Part 2: Rock Paper Scissors."""

from textwrap import dedent

from src.year2022.day02b import solve


def test_solve():
    task = dedent(
        """
        A Y
        B X
        C Z
        """
    ).strip()
    assert solve(task) == 12
