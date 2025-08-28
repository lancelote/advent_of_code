"""2018 - Day 5 Part 1: Alchemical Reduction."""

import pytest

from src.year2018.day05a import react, solve


@pytest.mark.parametrize(
    ("char1", "char2", "expected"),
    [
        ("a", "A", True),
        ("A", "a", True),
        ("a", "a", False),
        ("A", "A", False),
        ("B", "A", False),
        ("b", "b", False),
    ],
)
def test_react(char1, char2, expected):
    assert react(char1, char2) == expected


@pytest.mark.parametrize(
    ("task", "expected"),
    [
        ("dabAcCaCBAcCcaDA", 10),
        ("aA", 0),
        ("abBA", 0),
        ("abAB", 4),
        ("aabAAB", 6),
    ],
)
def test_solve(task, expected):
    assert solve(task) == expected
