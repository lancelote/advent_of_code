# pylint: disable=no-self-use

"""2017 - Day 3 Part 2: Spiral Memory."""

import pytest

from src.year2017.day3b import Memory


@pytest.fixture(name='memory')
def fixture_memory():
    return Memory()


@pytest.mark.parametrize(
    ('circle', 'expected'),
    [
        (0, 1),
        (1, 3),
        (2, 5),
        (3, 7),
    ]
)
def test_side_length(memory, circle, expected):
    memory.circle = circle
    assert memory.side_length == expected


@pytest.mark.parametrize(
    ('x', 'y', 'expected'),
    [
        (0, 0, [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]),
        (1, 1, [(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2)])
    ]
)
def test_neighbors(x, y, expected):
    assert Memory.neighbors(x, y) == expected


@pytest.mark.parametrize(
    ('side', 'expected'),
    [
        (0, (0, 1)),
        (1, (-1, 0)),
        (2, (0, -1)),
        (3, (1, 0))
    ]
)
def test_shift(memory, side, expected):
    memory.shift(side)
    assert (memory.dx, memory.dy) == expected


def test_next_item(memory):
    for i, item in enumerate(memory):
        print(item)
        if i == 5:
            raise ValueError
