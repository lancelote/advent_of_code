"""2015 - Day 12 Part 2: JSAbacusFramework.io."""

import pytest

from src.year2015.day12b import Lexer
from src.year2015.day12b import Number
from src.year2015.day12b import Symbol
from src.year2015.day12b import solve


@pytest.mark.parametrize(
    "task,expected",
    (
        (
            "[1,2,3]",
            [Symbol.OPEN, Number(1), Number(2), Number(3), Symbol.CLOSE],
        ),
        (
            '[1,{"c":"red","b":2},3]',
            [
                Symbol.OPEN,
                Number(1),
                Symbol.OPEN,
                Symbol.RED,
                Number(2),
                Symbol.CLOSE,
                Number(3),
                Symbol.CLOSE,
            ],
        ),
        (
            '{"d":"red","e":[1,2,3,4],"f":5}',
            [
                Symbol.OPEN,
                Symbol.RED,
                Symbol.OPEN,
                Number(1),
                Number(2),
                Number(3),
                Number(4),
                Symbol.CLOSE,
                Number(5),
                Symbol.CLOSE,
            ],
        ),
        (
            '[1,"red",5]',
            [
                Symbol.OPEN,
                Number(1),
                Number(5),
                Symbol.CLOSE,
            ],
        ),
    ),
)
def test_lexer(task, expected):
    lexer = Lexer(task)
    assert list(lexer) == expected


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
