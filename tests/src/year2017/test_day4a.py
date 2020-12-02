"""2017 - Day 4 Part 1: High-Entropy Passphrases tests."""
import pytest

from src.year2017.day4a import count_valid
from src.year2017.day4a import duplicates


@pytest.mark.parametrize(
    ("task", "expected"),
    [
        ("aa aa\ncc cc", 0),
        ("aa cc\naa bb\ncc cc", 2),
        ("a\nc b a\na aa", 3),
    ],
)
def test_count_valid(task, expected):
    assert count_valid(task, valid=duplicates) == expected


@pytest.mark.parametrize(
    ("passphrase", "expected"),
    [
        ("a aa", True),
        ("a a", False),
        ("bb bb", False),
        ("a b c d a", False),
    ],
)
def test_are_duplicates(passphrase, expected):
    assert duplicates(passphrase) == expected
