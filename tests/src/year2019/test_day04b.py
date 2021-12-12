"""2019 - Day 4 Part 2: Secure Container tests."""
import pytest

from src.year2019.day04b import at_least_one_equal_pair


@pytest.mark.parametrize(
    "num,expected",
    [
        ("112233", True),
        ("123444", False),
        ("111122", True),
    ],
)
def test_at_least_one_equal_pair(num, expected):
    assert at_least_one_equal_pair(num) is expected
