"""2021 - Day 3 Part 2: Binary Diagnostic."""

from textwrap import dedent

from src.year2021.day03b import solve


def test_solve():
    task = dedent(
        """
        00100
        11110
        10110
        10111
        10101
        01111
        00111
        11100
        10000
        11001
        00010
        01010
        """
    ).strip()
    assert solve(task) == 230
