"""2015 - Day 5 Part 1: Doesn't He Have Intern-Elves For This."""

import pytest

from src.year2015.day05b import is_nice


@pytest.mark.parametrize(
    "word,expected",
    (
        ("qjhvhtzxzqqjkmpb", True),
        ("xxyxx", True),
        ("uurcxstgmygtbstg", False),
        ("ieodomkazucvgmuy", False),
        ("aaa", False),
    ),
)
def test_returns_correct_result(word, expected):
    assert is_nice(word) is expected
