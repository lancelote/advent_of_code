"""2015 - Day 8 Part 2: Matchsticks."""

from textwrap import dedent

from src.year2015.day08b import solve


def test_solve():
    task = dedent(
        r"""
        ""
        "abc"
        "aaa\"aaa"
        "\x27"
        """
    ).strip()

    assert solve(task) == 19
