"""2018 - Day 6 Part 1: Chronal Coordinates tests."""

from textwrap import dedent

import pytest

from src.year2018.day06a import Coordinate, Dot, Grid, Pin


@pytest.fixture
def sample_task():
    return dedent(
        """
        1, 1
        1, 6
        8, 3
        3, 4
        5, 5
        8, 9
    """
    )


@pytest.fixture
def sample_grid():
    pins = [Pin(1, 1), Pin(1, 6), Pin(8, 3), Pin(3, 4), Pin(5, 5), Pin(8, 9)]
    width = 9
    height = 10
    dots = []
    for x in range(width):
        for y in range(height):
            dots.append(Dot(x, y))
    return Grid(pins, dots, width, height)


@pytest.mark.parametrize(
    ("coordinate1", "coordinate2", "distance"),
    [
        (Coordinate(0, 0), Coordinate(2, 3), 5),
        (Coordinate(2, 3), Coordinate(0, 0), 5),
        (Coordinate(1, 1), Coordinate(1, 1), 0),
    ],
)
def test_manhattan(coordinate1, coordinate2, distance):
    assert coordinate1 - coordinate2 == distance


class TestPin:
    @pytest.mark.parametrize(
        ("line", "pin"),
        [
            ("79, 66", Pin(79, 66)),
            ("72, 281", Pin(72, 281)),
            ("251, 337", Pin(251, 337)),
        ],
    )
    def test_from_string(self, line, pin):
        assert Pin.from_string(line) == pin

    def test_parse_task(self, sample_task):
        expected_pins = [
            Pin(1, 1),
            Pin(1, 6),
            Pin(8, 3),
            Pin(3, 4),
            Pin(5, 5),
            Pin(8, 9),
        ]
        assert Pin.parse_task(sample_task) == expected_pins


class TestGrid:
    def test_parse_task(self, sample_task, sample_grid):
        assert Grid.parse_task(sample_task) == sample_grid

    def test_largest_area(self, sample_grid):
        assert sample_grid.largest_area == 17
