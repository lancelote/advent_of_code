"""2023 - Day 3 Part 1: Gear Ratios"""
from textwrap import dedent

from src.year2023.day03a import solve


def test_solve():
    task = dedent(
        """
        467..114..
        ...*......
        ..35..633.
        ......#...
        617*......
        .....+.58.
        ..592.....
        ......755.
        ...$.*....
        .664.598..
        """
    ).strip()
    assert solve(task) == 4361
