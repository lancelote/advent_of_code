"""2015 - Day 1 Part 1: Not Quite Lisp."""

import pytest

from src.year2015.day01a import solve


@pytest.mark.parametrize(
    "task,expected",
    (
        ("(())", 0),
        ("()()", 0),
        ("(((", 3),
        ("(()(()(", 3),
        ("))(((((", 3),
        ("())", -1),
        ("))(", -1),
        (")))", -3),
        (")())())", -3),
    ),
)
def test_solve(task, expected):
    assert solve(task) == expected
