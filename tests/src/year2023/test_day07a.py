"""2023 - Day 7 Part 1: Camel Cards"""
from textwrap import dedent

from src.year2023.day07a import solve


def test_solve():
    task = dedent(
        """
        32T3K 765
        T55J5 684
        KK677 28
        KTJJT 220
        QQQJA 483
        """
    ).strip()
    assert solve(task) == 6440
