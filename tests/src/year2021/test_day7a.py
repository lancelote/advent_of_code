"""2021 - Day 7 Part 1: The Treachery of Whales."""
from textwrap import dedent

from src.year2021.day7a import solve


def test_solve():
    task = dedent(
        """
        16,1,2,0,4,2,7,1,2,14
        """.strip()
    )
    assert solve(task) == 37
