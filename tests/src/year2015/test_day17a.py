"""2015 - Day 17 Part 1: No Such Thing as Too Much."""

from src.year2015.day17a import count_options
from src.year2015.day17a import process_data


def test_process_data():
    assert process_data("20\n15\n10\n5\n5") == [20, 15, 10, 5, 5]


def test_count_options():
    assert count_options([20, 15, 10, 5, 5], 25) == 4
