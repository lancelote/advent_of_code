"""2015 - Day 12 Part 2: JSAbacusFramework.io."""

import pytest

from src.year2015.day12b import Parser
from src.year2015.day12b import solve


@pytest.mark.parametrize(
    "task,expected",
    (
        ("[1,2,3]", [1, 2, 3]),
        ('[1,{"c":"red","b":2},3]', [1, {"c": "red", "b": 2}, 3]),
        (
            '{"d":"red","e":[1,2,3,4],"f":5}',
            {"d": "red", "e": [1, 2, 3, 4], "f": 5},
        ),
        ('[1,"red",5]', [1, "red", 5]),
        ("[-1,-2]", [-1, -2]),
    ),
)
def test_parser(task, expected):
    assert Parser(task).parse_expression() == expected


@pytest.mark.parametrize(
    "task,expected",
    (
        ("[1,2,3]", 6),
        ('[1,{"c":"red","b":2},3]', 4),
        ('{"d":"red","e":[1,2,3,4],"f":5}', 0),
        ('[1,"red",5]', 6),
    ),
)
def test_solve(task, expected):
    assert solve(task) == expected
