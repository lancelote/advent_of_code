"""2024 - Day 14 Part 1: Restroom Redoubt"""

from textwrap import dedent

from src.year2024.day14a import solve


def test_solve():
    task = dedent(
        """
        p=0,4 v=3,-3
        p=6,3 v=-1,-3
        p=10,3 v=-1,2
        p=2,0 v=2,-1
        p=0,0 v=1,3
        p=3,0 v=-2,-2
        p=7,6 v=-1,-3
        p=3,0 v=-1,-2
        p=9,3 v=2,3
        p=7,3 v=-1,2
        p=2,4 v=2,-3
        p=9,5 v=-3,-3
        """
    ).strip()
    assert solve(task, width=11, height=7) == 12
