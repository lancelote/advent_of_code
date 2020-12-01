"""2020 - Day 1 Part 2: Report Repair."""

import pytest

from src.year2020.day1b import solve


@pytest.mark.parametrize(
    "task,expected",
    [
        ("1721\n979\n366\n299\n675\n1456\n", 241_861_950),
    ],
)
def test_solve(task, expected):
    assert solve(task) == expected
