"""2025 - Day 4 Part 2: Printing Department"""

from textwrap import dedent

from src.year2025.day04b import solve


def test_solve():
    task = dedent(
        """
        ..@@.@@@@.
        @@@.@.@.@@
        @@@@@.@.@@
        @.@@@@..@.
        @@.@@@@.@@
        .@@@@@@@.@
        .@.@.@.@@@
        @.@@@.@@@@
        .@@@@@@@@.
        @.@.@@@.@.
        """
    ).strip()
    assert solve(task) == 43
