"""2020 - Day 16 Part 1: Ticket Translation."""
from textwrap import dedent

from src.year2020.day16a import solve


def test_solve():
    task = dedent(
        """
        class: 1-3 or 5-7
        row: 6-11 or 33-44
        seat: 13-40 or 45-50

        your ticket:
        7,1,14

        nearby tickets:
        7,3,47
        40,4,50
        55,2,20
        38,6,12
    """
    ).strip()
    assert solve(task) == 71
