"""2015 - Day 14 Part 1: Reindeer Olympics."""

import pytest

from src.year2015.day14a import Reindeer


@pytest.fixture
def comet():
    return Reindeer(14, 10, 127)


@pytest.fixture
def dancer():
    return Reindeer(16, 11, 162)


@pytest.mark.parametrize(
    "seconds,expected",
    (
        (1, 14),
        (10, 140),
        (11, 140),
        (12, 140),
        (1000, 1120),
    ),
)
def test_comet(comet, seconds, expected):
    assert comet.distance_after(seconds) == expected


@pytest.mark.parametrize(
    "seconds,expected",
    (
        (1, 16),
        (10, 160),
        (11, 176),
        (12, 176),
        (1000, 1056),
    ),
)
def test_dancer(dancer, seconds, expected):
    assert dancer.distance_after(seconds) == expected
