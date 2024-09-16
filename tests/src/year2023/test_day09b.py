"""2023 - Day 9 Part 2: Mirage Maintenance"""

from textwrap import dedent

import pytest

from src.year2023.day09b import get_prev_value
from src.year2023.day09b import solve


@pytest.mark.parametrize(
    "hist,expected",
    (
        ([0, 3, 6, 9, 12, 15], -3),
        ([1, 3, 6, 10, 15, 21], 0),
        ([10, 13, 16, 21, 30, 45], 5),
    ),
)
def test_get_next_value(hist, expected):
    assert get_prev_value(hist) == expected


def test_solve():
    task = dedent(
        """
        0 3 6 9 12 15
        1 3 6 10 15 21
        10 13 16 21 30 45
        """
    ).strip()
    assert solve(task) == 2
