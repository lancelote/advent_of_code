"""2023 - Day 7 Part 1: Camel Cards"""
from textwrap import dedent

import pytest

from src.year2023.day07a import Hand
from src.year2023.day07a import solve


@pytest.mark.parametrize(
    "a,b",
    (
        ("2AAAA", "33332"),
        ("77788", "77888"),
    ),
)
def test_compare(a, b):
    assert Hand(a) < Hand(b)


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
