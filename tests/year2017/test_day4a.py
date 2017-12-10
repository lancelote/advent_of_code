# pylint: disable=no-self-use

"""2017 - Day 4 Part 1: High-Entropy Passphrases tests."""

import pytest

from src.year2017.day4a import solve, valid


@pytest.mark.parametrize(
    ('task', 'expected'),
    [
        ('aa aa\ncc cc', 0),
        ('aa cc\naa bb\ncc cc', 2),
        ('a\nc b a\na aa', 3),
    ]
)
def test_solve(task, expected):
    assert solve(task) == expected


@pytest.mark.parametrize(
    ('passphrase', 'expected'),
    [
        ('a aa', True),
        ('a a', False),
        ('bb bb', False),
        ('a b c d a', False),
    ]
)
def test_valid(passphrase, expected):
    assert valid(passphrase) == expected
