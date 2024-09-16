"""2020 - Day 6 Part 2: Custom Customs."""

from textwrap import dedent

from src.year2020.day06b import solve


def test_solve():
    task = dedent(
        """
        abc

        a
        b
        c

        ab
        ac

        a
        a
        a
        a

        b
        """
    )
    assert solve(task) == 6
