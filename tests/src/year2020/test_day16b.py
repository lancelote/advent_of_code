"""2020 - Day 16 Part 2: Ticket Translation."""
from textwrap import dedent

from src.year2020.day16b import solve


def test_solve():
    task = dedent(
        """
        departure class: 0-1 or 4-19
        departure row: 0-5 or 8-19
        departure seat: 0-13 or 16-19

        your ticket:
        11,12,13

        nearby tickets:
        3,9,18
        15,1,5
        5,14,9
        """
    ).strip()
    assert solve(task) == 12 * 11 * 13
