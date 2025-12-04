"""2025 - Day 4 Part 1: Printing Department"""

from textwrap import dedent

from src.year2025.day04a import solve


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
    assert solve(task) == 13
