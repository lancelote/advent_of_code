"""2015 - Day 13 Part 2: Knights of the Dinner Table."""

from src.year2015.day13b import solve
from tests.src.year2015.test_day13a import EXAMPLE


def test_solve():
    assert solve(EXAMPLE) == 286
