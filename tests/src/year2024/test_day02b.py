"""2024 - Day 2 Part 2: Red-Nosed Reports"""

from textwrap import dedent

import pytest

from src.year2024.day02b import is_decreasing
from src.year2024.day02b import is_increasing
from src.year2024.day02b import solve


def test_solve():
    task = dedent(
        """
        7 6 4 2 1
        1 2 7 8 9
        9 7 6 2 1
        1 3 2 4 5
        8 6 4 4 1
        1 3 6 7 9
        """.strip()
    )
    assert solve(task) == 4


@pytest.mark.parametrize(
    "level,is_incr,is_decr",
    (
        ([1, 1, 1, 2], False, False),
        ([1, 1, 9], False, False),
        ([9, 1, 10], True, False),
        ([9, 1, 2], True, False),
        ([9, 5, 6, 7], True, False),
        ([1, 9, 8, 7], False, True),
        ([1, 2, 3, 9], True, False),
        ([1, 2, 3, 9, 10], False, False),
        ([1, 3, 2, 4, 5], True, False),
        ([1, 2, 3, 4, 1], True, False),
    ),
)
def test_is_safe(level, is_incr, is_decr):
    assert is_increasing(level) is is_incr
    assert is_decreasing(level) is is_decr
