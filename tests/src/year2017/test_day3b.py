"""2017 - Day 3 Part 2: Spiral Memory."""
import itertools

import pytest

from src.year2017.day3b import Memory
from src.year2017.day3b import solve


@pytest.fixture(name="memory")
def fixture_memory():
    return Memory()


@pytest.mark.parametrize(
    ("circle", "expected"),
    [
        (0, 1),
        (1, 3),
        (2, 5),
        (3, 7),
    ],
)
def test_side_length(memory, circle, expected):
    memory.circle = circle
    assert memory.side_length(0) == expected - 1
    assert memory.side_length(1) == expected
    assert memory.side_length(2) == expected
    assert memory.side_length(3) == expected + 1


@pytest.mark.parametrize(
    ("x", "y", "expected"),
    [
        (
            0,
            0,
            [
                (-1, -1),
                (-1, 0),
                (-1, 1),
                (0, -1),
                (0, 1),
                (1, -1),
                (1, 0),
                (1, 1),
            ],
        ),
        (
            1,
            1,
            [(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2)],
        ),
    ],
)
def test_neighbors(x, y, expected, memory):
    memory.x = x
    memory.y = y
    assert list(memory.neighbors) == expected


@pytest.mark.parametrize(
    ("side", "expected"),
    [(0, (0, 1)), (1, (-1, 0)), (2, (0, -1)), (3, (1, 0))],
)
def test_adjust_direction(memory, side, expected):
    memory.adjust_direction(side)
    assert (memory.dx, memory.dy) == expected


def test_next_item(memory):
    assert list(itertools.islice(memory, 23)) == [
        1,
        1,
        2,
        4,
        5,
        10,
        11,
        23,
        25,
        26,
        54,
        57,
        59,
        122,
        133,
        142,
        147,
        304,
        330,
        351,
        362,
        747,
        806,
    ]


def test_solve():
    assert solve("368078") == 369601
