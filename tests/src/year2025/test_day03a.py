"""2025 - Day 3 Part 1: Lobby"""

from textwrap import dedent

from src.year2025.day03a import solve


def test_solve():
    task = dedent(
        """
        987654321111111
        811111111111119
        234234234234278
        818181911112111
        """
    ).strip()
    assert solve(task) == 357
