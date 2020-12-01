"""Day 11 Part 2: Chronal Charge."""

import pytest

from src.year2018.day11b import CachedGrid


@pytest.fixture(scope="session")
def grid():
    return CachedGrid(serial=1, side=3)


@pytest.mark.parametrize(
    ("x", "y", "size", "expected_power"),
    [
        (0, 0, 2, -13),
        (0, 0, 3, -17),
        (1, 1, 2, -9),
        (1, 0, 2, -13),
        (0, 1, 2, -10),
    ],
)
def test_get_border_power(x, y, size, expected_power, grid):
    assert grid.get_border_power(x, y, size) == expected_power


@pytest.mark.parametrize(
    ("x", "y", "size", "expected_power"),
    [
        (0, 0, 1, -5),
        (0, 0, 2, -18),
        (0, 0, 3, -35),
        (1, 1, 2, -13),
        (0, 1, 2, -14),
        (1, 0, 2, -18),
    ],
)
def test_square_power(x, y, size, expected_power, grid):
    assert grid.get_square_power(x, y, size) == expected_power
