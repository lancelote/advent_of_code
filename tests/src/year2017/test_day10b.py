"""2017 - Day 10 Part 2: Knot Hash tests."""

import pytest

from src.year2017.day10b import compress
from src.year2017.day10b import process_data
from src.year2017.day10b import solve
from src.year2017.day10b import split
from src.year2017.day10b import to_hex


def test_process_data():
    assert process_data("1,2,3") == [49, 44, 50, 44, 51]


@pytest.mark.parametrize(
    ("sequence", "chunk", "expected"),
    [
        ([0, 1, 2, 3], 2, [[0, 1], [2, 3]]),
        ([0, 1, 2, 3, 4, 5, 6, 7, 8], 3, [[0, 1, 2], [3, 4, 5], [6, 7, 8]]),
    ],
)
def test_split(sequence, chunk, expected):
    assert split(sequence, chunk) == expected


def test_compress():
    assert compress([0, 1, 2, 3, 4, 5, 6, 7, 8], chunk=3) == [3, 2, 9]


@pytest.mark.parametrize(("number", "expected"), [(64, "40"), (7, "07"), (255, "ff")])
def test_to_hex(number, expected):
    assert to_hex(number) == expected


@pytest.mark.parametrize(
    ("message", "expected"),
    [
        ("", "a2582a3a0e66e6e86e3812dcb672a272"),
        ("AoC 2017", "33efeb34ea91902bb2f59c9920caa6cd"),
        ("1,2,3", "3efbe78a8d82f29979031a4aa0b16a9d"),
        ("1,2,4", "63960835bcdc130f0b66d7ff4f6a5a8e"),
    ],
)
def test_solve(message, expected):
    assert solve(message) == expected
