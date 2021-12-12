"""2020 - Day 9 Part 2: Encoding Error."""
from textwrap import dedent

from src.year2020.day09b import solve


def test_solve():
    task = dedent(
        """
        35
        20
        15
        25
        47
        40
        62
        55
        65
        95
        102
        117
        150
        182
        127
        219
        299
        277
        309
        576
        """
    )
    assert solve(task, preamble_length=5) == 62
