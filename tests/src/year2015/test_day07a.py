"""2015 - Day 7 Part 1: Some Assembly Required."""
from textwrap import dedent

from src.year2015.day07a import solve


def test_solve():
    task = dedent(
        """
        h -> a
        123 -> x
        456 -> y
        x AND y -> d
        x OR y -> e
        x LSHIFT 2 -> f
        y RSHIFT 2 -> g
        NOT x -> h
        NOT y -> i
        """
    ).strip()
    assert solve(task) == 65412
