"""2019 - Day 4 Part 1: Secure Container tests."""
import pytest

from src.year2019.day4a import never_decrease
from src.year2019.day4a import process_data
from src.year2019.day4a import two_adjacent


def test_process_data():
    start, stop = process_data("246515-739105")
    assert (start, stop) == (246515, 739105)


@pytest.mark.parametrize(
    "num,expected",
    [
        ("223450", False),
        ("111111", True),
        ("123789", True),
        ("102345", False),
    ],
)
def test_not_decrease(num, expected):
    assert never_decrease(num) is expected


@pytest.mark.parametrize(
    "num,expected",
    [
        ("111111", True),
        ("223450", True),
        ("123789", False),
        ("122345", True),
    ],
)
def test_two_next(num, expected):
    assert two_adjacent(num) is expected
