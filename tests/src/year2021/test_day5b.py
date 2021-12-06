"""2021 - Day 5 Part 2: Hydrothermal Venture."""
from textwrap import dedent

from src.year2021.day5b import solve


def test_solve():
    task = dedent(
        """
        0,9 -> 5,9
        8,0 -> 0,8
        9,4 -> 3,4
        2,2 -> 2,1
        7,0 -> 7,4
        6,4 -> 2,0
        0,9 -> 2,9
        3,4 -> 1,4
        0,0 -> 8,8
        5,5 -> 8,2
        """.strip()
    )
    assert solve(task) == 12
