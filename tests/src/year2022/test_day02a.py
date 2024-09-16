"""2022 - Day 2 Part 1: Rock Paper Scissors."""

from textwrap import dedent

from src.year2022.day02a import solve


def test_solve():
    task = dedent(
        """
        A Y
        B X
        C Z
        """
    ).strip()
    assert solve(task) == 15
