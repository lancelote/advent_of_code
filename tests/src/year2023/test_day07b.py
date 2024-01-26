"""2023 - Day 7 Part 2: Camel Cards"""
from textwrap import dedent

import pytest

from src.year2023.day07b import Hand
from src.year2023.day07b import solve


@pytest.mark.parametrize(
    "cards,expected_value",
    (
        ("32T3K", 13),  # one pair
        ("T55J5", 17),  # four of a kind
        ("KK677", 14),  # two pair
        ("KTJJT", 17),  # four of a kind
        ("QQQJA", 17),  # four of a kind
    ),
)
def test_compare(cards, expected_value):
    assert Hand(cards).value == expected_value


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
    assert solve(task) == 5905
