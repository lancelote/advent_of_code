"""2015 - Day 5 Part 1: Doesn't He Have Intern-Elves For This."""

import pytest

from src.year2015.day05a import is_nice, process_data


@pytest.mark.parametrize(
    "word,expected",
    (
        ("ugknbfddgicrmopn", True),
        ("aaa", True),
        ("jchzalrnumimnmhp", False),
        ("haegwjzuvuyypxyu", False),
        ("dvszwmarrgswjxmb", False),
    ),
)
def test_returns_correct_result(word, expected):
    assert is_nice(word) is expected


@pytest.mark.parametrize(
    "task,expected",
    (
        ("ab\ncd\n", ["ab", "cd"]),
        ("ab", ["ab"]),
    ),
)
def test_process_data(task, expected):
    assert process_data(task) == expected
