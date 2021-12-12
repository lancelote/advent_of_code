"""2018 - Day 1 Part 1: Chronal Calibration tests."""
from src.year2018.day01a import process_data
from src.year2018.day01a import solve


def test_process_data():
    assert list(process_data("+1\n0\n-2\n2\n")) == [1, 0, -2, 2]


def test_solve():
    assert solve("+1\n0\n-2\n2\n") == 1
