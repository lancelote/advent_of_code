# pylint: disable=no-self-use

"""2017 - Day 2 Part 1: Corruption Checksum tests."""

import pytest

from src.year2017.day2a import process_data, solve


@pytest.fixture(name='data')
def fixture_data():
    return """5	1	9	5
    7	5	3
    2	4	6	8"""


def test_big_example(data):
    assert process_data(data) == [[5, 1, 9, 5], [7, 5, 3], [2, 4, 6, 8]]


def test_solve(data):
    assert solve(data) == 18
