"""2015 - Day 11 Part 1: Corporate Policy."""

import pytest

from src.year2015.day11b import Number
from src.year2015.day11b import solve


@pytest.mark.parametrize(
    "line,expected",
    (
        ("hepyyzaa", False),
        ("hepxxyzz", True),
    ),
)
def test_is_valid(line, expected):
    assert Number.from_line(line).is_valid is expected


def test_solve():
    assert solve("hepxcrrq") == "heqaabcc"
