# pylint: disable=no-self-use

"""2017 - Day 3 Part 1: Spiral Memory tests."""

import pytest

from src.year2017.day3a import solve, get_circle_number, get_deviation


class TestSolve:

    def test_start(self):
        assert solve('1') == 0

    def test_not_proper_diagonal(self):
        assert solve('12') == 3

    def test_vertical(self):
        assert solve('23') == 2

    def test_big_number(self):
        assert solve('1024') == 31


@pytest.mark.parametrize(
    ('number', 'expected'),
    [
        (1, 0),
        *((i, 1) for i in range(2, 10)),
        *((i, 2) for i in range(10, 26)),
        *((i, 3) for i in range(26, 50)),
        (50, 4),
    ]
)
def test_circle_number(number, expected):
    assert get_circle_number(number) == expected


@pytest.mark.parametrize(
    ('number', 'circle', 'expected'),
    [
        (1, 0, 0),
        (2, 1, 0),
        (3, 1, 1),
        (4, 1, 0),
        (5, 1, 1),
        (6, 1, 0),
        (7, 1, 1),
        (8, 1, 0),
        (9, 1, 1),
        (10, 2, 1),
        (11, 2, 0),
        (12, 2, 1),
        (13, 2, 2),
        (14, 2, 1),
        (15, 2, 0),
        (16, 2, 1),
        (17, 2, 2),
        (18, 2, 1),
        (19, 2, 0),
        (20, 2, 1),
        (21, 2, 2),
        (22, 2, 1),
        (23, 2, 0),
        (24, 2, 1),
        (25, 2, 2),
    ]
)
def test_get_deviation(number, circle, expected):
    assert get_deviation(number, circle) == expected
