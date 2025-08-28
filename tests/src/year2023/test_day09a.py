"""2023 - Day 9 Part 1: Mirage Maintenance"""

from textwrap import dedent

import pytest

from src.year2023.day09a import get_next_value, solve


@pytest.mark.parametrize(
    "hist,expected",
    (
        ([0, 3, 6, 9, 12, 15], 18),
        ([1, 3, 6, 10, 15, 21], 28),
        ([10, 13, 16, 21, 30, 45], 68),
    ),
)
def test_get_next_value(hist, expected):
    assert get_next_value(hist) == expected


def test_solve():
    task = dedent(
        """
        0 3 6 9 12 15
        1 3 6 10 15 21
        10 13 16 21 30 45
        """
    ).strip()
    assert solve(task) == 114
