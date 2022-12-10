"""2022 - Day 9 Part 1: Rope Bridge."""
from textwrap import dedent

import pytest

from src.year2022.day09a import solve
from src.year2022.day09a import update_tail


@pytest.mark.parametrize(
    "head,tail,expected",
    [
        ((0, 0), (0, 0), (0, 0)),
        ((0, 2), (0, 0), (0, 1)),
        ((2, 0), (0, 0), (1, 0)),
        ((1, 1), (0, 0), (0, 0)),
        ((2, 1), (0, 0), (1, 1)),
        ((0, 0), (2, 2), (1, 1)),
        ((0, 0), (0, 2), (0, 1)),
    ],
)
def test_update_tail(head, tail, expected):
    assert update_tail(head, tail) == expected


def test_solve():
    task = dedent(
        """
        R 4
        U 4
        L 3
        D 1
        R 4
        D 1
        L 5
        R 2
        """
    ).strip()
    assert solve(task) == 13
