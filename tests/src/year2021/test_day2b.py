"""2021 - Day 2 Part 2: Dive!"""
from textwrap import dedent

from src.year2021.day2b import solve


def test_solve():
    task = dedent(
        """
        forward 5
        down 5
        forward 8
        up 3
        down 8
        forward 2
        """
    ).strip()
    assert solve(task) == 900
