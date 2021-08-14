"""2020 - Day 15 Part 1: Rambunctious Recitation."""
import pytest

from src.year2020.day15a import solve


@pytest.mark.parametrize(
    "task,expected_last",
    [
        ("0,3,6", 436),
        ("1,3,2", 1),
        ("2,1,3", 10),
        ("1,2,3", 27),
        ("2,3,1", 78),
        ("3,2,1", 438),
        ("3,1,2", 1836),
    ],
)
def test_solve(task, expected_last):
    assert solve(task) == expected_last
