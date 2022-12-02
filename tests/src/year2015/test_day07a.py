"""Day 7 Puzzle Part 1 tests."""
from textwrap import dedent

from src.year2015.day07a import solve


def test_solve():
    task = dedent(
        """
        h -> z
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
    assert solve(task, "z") == 65412
