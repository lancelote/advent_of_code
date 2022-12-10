"""2022 - Day 8 Part 2: Treetop Tree House."""
from textwrap import dedent

from src.year2022.day08b import solve


def test_solve():
    task = dedent(
        """
        30373
        25512
        65332
        33549
        35390
        """
    ).strip()
    assert solve(task) == 8
