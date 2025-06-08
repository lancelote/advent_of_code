"""2015 - Day 8 Part 1: Matchsticks."""

from textwrap import dedent

from src.year2015.day08a import solve


def test_solve():
    task = dedent(
        r"""
        ""
        "abc"
        "aaa\"aaa"
        "\x27"
        """
    ).strip()

    assert solve(task) == 12
