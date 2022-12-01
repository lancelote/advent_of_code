"""2022 - Day 1 Part 2: Calorie Counting."""
from textwrap import dedent

from src.year2022.day01b import solve


def test_solve():
    task = dedent(
        """
        1000
        2000
        3000

        4000

        5000
        6000

        7000
        8000
        9000

        10000
        """.strip()
    )
    assert solve(task) == 45000
