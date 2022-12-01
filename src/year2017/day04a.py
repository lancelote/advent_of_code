"""2017 - Day 4 Part 1: High-Entropy Passphrases.

A new system policy has been put in place that requires all accounts to use a
passphrase instead of simply a password. A passphrase consists of a series of
words (lowercase letters) separated by spaces.

To ensure security, a valid passphrase must contain no duplicate words.

For example:

    - "aa bb cc dd ee" is valid.
    - "aa bb cc dd aa" is not valid - the word aa appears more than once.
    - "aa bb cc dd aaa" is valid - aa and aaa count as different words.

The system's full passphrase list is available as your puzzle input. How many
passphrases are valid?
"""
from collections.abc import Callable


def duplicates(passphrase: str) -> bool:
    """Check if passphrase is valid."""
    words = passphrase.split()
    return len(words) == len(set(words))


def count_valid(passphrases: str, valid: Callable[[str], bool]) -> int:
    """Count valid passphrases."""
    result = 0
    for passphrase in passphrases.strip().split("\n"):
        if valid(passphrase):
            result += 1
    return result


def solve(task: str) -> int:
    """Count number of passphrases without duplicates."""
    return count_valid(task, valid=duplicates)
