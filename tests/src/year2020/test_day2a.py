"""2020 - Day 2 Part 1: Password Philosophy."""
import pytest

from src.year2020.day2a import solve


@pytest.mark.parametrize(
    "task,expected",
    [
        ("1-3 a: abcde\n1-3 b: cdefg\n2-9 c: ccccccccc", 2),
    ],
)
def test_solve(task, expected):
    assert solve(task) == expected
