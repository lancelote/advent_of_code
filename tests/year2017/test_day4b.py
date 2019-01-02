"""2017 - Day 4 Part 2: High-Entropy Passphrases tests."""

import pytest

from src.year2017.day4b import anagrams


@pytest.mark.parametrize(
    ('passphrase', 'expected'),
    [
        ('abcde fghij', True),
        ('abcde xyz ecdab', False),
        ('a ab abc abd abf abj', True),
        ('iiii oiii ooii oooi oooo', True),
        ('oiii ioii iioi iiio', False)
    ]
)
def test_anagrams(passphrase, expected):
    assert anagrams(passphrase) == expected
