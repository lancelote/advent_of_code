"""2017 - Day 10 Part 1: Knot Hash tests."""

import pytest

from src.year2017.day10a import Rope
from src.year2017.day10a import process_data


@pytest.fixture(name="rope")
def fixture_rope():
    return Rope([0, 1, 2, 3, 4])


@pytest.mark.parametrize(
    ("rope", "expected"),
    [
        (Rope([1, 2, 3]), 2),
        (Rope([3, 4, 5]), 12),
        (Rope([2, 0, 1]), 0),
    ],
)
def test_first_two_multiply(rope, expected):
    assert rope.first_two_multiply() == expected


def test_reverse(rope):
    lengths = [3, 4, 1, 5]
    shapes = [
        [2, 1, 0, 3, 4],
        [4, 3, 0, 1, 2],
        [4, 3, 0, 1, 2],
        [3, 4, 2, 1, 0],
    ]
    for length, shape in zip(lengths, shapes):
        rope.reverse(length)
        rope.move(length)
        assert rope.nodes == shape


def test_move(rope):
    lengths = [3, 4, 1, 5]
    positions = [3, 3, 1, 4]
    assert rope.pos == 0
    for length, position in zip(lengths, positions):
        rope.move(length)
        assert rope.pos == position


def test_process_data():
    assert process_data("1,2,3\n") == [1, 2, 3]
