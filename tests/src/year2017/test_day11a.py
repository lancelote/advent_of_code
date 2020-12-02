"""2017 - Day 11 Part 1: Hex Edh test."""
import pytest

from src.year2017.day11a import solve


@pytest.mark.parametrize(
    ("directions", "expected"),
    [
        ("ne,ne,ne", 3),
        ("ne,ne,sw,sw", 0),
        ("ne,ne,s,s", 2),
        ("se,sw,se,sw,sw", 3),
    ],
)
def test_solve(directions, expected):
    assert solve(directions) == expected
