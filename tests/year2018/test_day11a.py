"""Day 11 Part 1: Chronal Charge tests."""

import pytest

from src.year2018.day11a import get_power_level, solve, get_grid,\
    get_square_power, get_biggest_area


@pytest.mark.parametrize(
    ('x', 'y', 'serial', 'power_level'),
    [
        (3, 5, 8, 4),
        (122, 79, 57, -5),
        (217, 196, 39, 0),
        (101, 153, 71, 4),
    ]
)
def test_get_power_level(x, y, serial, power_level):
    assert get_power_level(x, y, serial) == power_level


def test_get_square_power():
    assert get_square_power(0, 0, get_grid(1, 3)) == -35


def test_biggest_area():
    assert get_biggest_area(3, get_grid(1, 3)) == (0, 0)


@pytest.mark.parametrize(
    ('serial', 'expected'),
    [
        ('18', (33, 45)),
        ('42', (21, 61)),
    ]
)
def test_solve(serial, expected):
    assert solve(serial) == expected
