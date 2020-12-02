"""Day 11 Part 1: Chronal Charge tests."""
import pytest

from src.year2018.day11a import solve


@pytest.mark.parametrize(
    ("serial", "expected"),
    [
        ("18", (33, 45)),
        ("42", (21, 61)),
    ],
)
def test_solve(serial, expected):
    assert solve(serial) == expected
