"""2020 - Day 5 Part 1: Binary Boarding."""
from textwrap import dedent

import pytest

from src.year2020.day5a import binary_search
from src.year2020.day5a import solve


@pytest.mark.parametrize(
    "start,stop,steps,expected",
    [
        (0, 127, "FBFBBFF", 44),
        (0, 127, "FBFBBFB", 45),
        (0, 7, "RLR", 5),
    ],
)
def test_binary_search(start, stop, steps, expected):
    assert binary_search(start, stop, steps) == expected


def test_solve():
    task = dedent(
        """
        FBFBBFFRLR
        BFFFBBFRRR
        FFFBBBFRRR
        BBFFBBFRLL
        """
    )
    assert solve(task) == 820
