"""2015 - Day 11 Part 1: Corporate Policy."""

import pytest

from src.year2015.day11a import has_two_pairs, incr, is_valid, to_num


@pytest.mark.parametrize(
    "num,expected",
    (
        ([25], [0, 1]),
        ([0], [1]),
        ([25, 25], [0, 0, 1]),
    ),
)
def test_incr(num, expected):
    incr(num)
    assert num == expected


@pytest.mark.parametrize(
    "num,expected",
    (
        ([0, 0, 1, 1], True),
        ([0, 1, 2], False),
        ([1, 1, 1, 1], False),
        ([1, 1, 1], False),
    ),
)
def test_has_two_pairs(num, expected):
    assert has_two_pairs(num) is expected


@pytest.mark.parametrize(
    "line,expected",
    (
        ("hijklmmn", False),
        ("abbceffg", False),
        ("abbcegjk", False),
        ("abcdffaa", True),
        ("ghjaabcc", True),
    ),
)
def test_is_valid(line, expected):
    assert is_valid(to_num(line)) is expected
