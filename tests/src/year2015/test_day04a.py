"""2015 - Day 4 Part 1: The Ideal Stocking Stuffer."""

import pytest

from src.year2015.day04a import solve


@pytest.mark.parametrize(
    "task,expected",
    (
        ("abcdef", 609043),
        ("pqrstuv", 1048970),
        ("yzbqklnj", 282749),
    ),
)
def test_returns_correct_result(task, expected):
    assert solve(task) == expected
