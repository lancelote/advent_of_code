"""2020 - Day 1 Part 1: Report Repair."""

import pytest

from src.year2020.day1a import process_data
from src.year2020.day1a import find_2020_summands
from src.year2020.day1a import solve


def test_process_data():
    data = "1721\n979\n366\n299\n675\n1456\n"
    assert process_data(data) == [1721, 979, 366, 299, 675, 1456]


@pytest.mark.parametrize(
    "numbers,expected",
    [
        ([1721, 979, 366, 299, 675, 1456], (1721, 299)),
    ],
)
def test_find_summands(numbers, expected):
    assert find_2020_summands(numbers) == expected


@pytest.mark.parametrize(
    "task,expected",
    [
        ("1721\n979\n366\n299\n675\n1456\n", 514579),
    ],
)
def test_solve(task, expected):
    assert solve(task) == expected
