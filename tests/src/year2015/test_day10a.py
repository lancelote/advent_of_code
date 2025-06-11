"""2015 - Day 10 Part 1: Elves Look, Elves Say."""

import pytest

from src.year2015.day10a import iterate


@pytest.mark.parametrize(
    "state,expected",
    (
        ([1], [1, 1]),
        ([1, 1], [2, 1]),
        ([2, 1], [1, 2, 1, 1]),
        ([1, 2, 1, 1], [1, 1, 1, 2, 2, 1]),
        ([1, 1, 1, 2, 2, 1], [3, 1, 2, 2, 1, 1]),
    ),
)
def test_iterate(state, expected):
    assert iterate(state) == expected
