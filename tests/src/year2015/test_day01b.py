"""2015 - Day 1 Part 2: Not Quite Lisp."""

import pytest

from src.year2015.day01b import solve


@pytest.mark.parametrize(
    "task,expected",
    (
        (")", 1),
        ("()())", 5),
    ),
)
def test_returns_correct_result(task, expected):
    assert solve(task) == expected
