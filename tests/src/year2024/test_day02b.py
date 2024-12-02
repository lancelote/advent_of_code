"""2024 - Day 2 Part 2:"""

from textwrap import dedent

import pytest

from src.year2024.day02b import solve
from src.year2024.day02b import is_safe


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
    "level,expected",
    (
        ([1, 1, 1, 2], False),
        ([1, 1], True),
        ([1, 1, 9], False),
        ([9, 1], True),
        ([9, 5, 6, 7], True),
    ),
)
def test_is_safe(level, expected):
    assert is_safe(level) is expected
