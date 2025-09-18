"""2015 - Day 17 Part 2: No Such Thing as Too Much."""

from src.year2015.day17b import count_options


def test_count_options():
    assert count_options([20, 15, 10, 5, 5], 25) == 3
