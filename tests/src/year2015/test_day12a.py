"""2015 - Day 12 Part 1: JSAbacusFramework.io."""

import pytest

from src.year2015.day12a import solve


@pytest.mark.parametrize(
    "task,expected",
    (
        ("[1,2,3]", 6),
        ('{"a":2,"b":4}', 6),
        ("[[[3]]]", 3),
        ('{"a":{"b":4},"c":-1}', 3),
        ('{"a":[-1,1]}', 0),
        ('[-1,{"a":1}]', 0),
        ("[]", 0),
        ("{}", 0),
    ),
)
def test_solve(task, expected):
    assert solve(task) == expected
