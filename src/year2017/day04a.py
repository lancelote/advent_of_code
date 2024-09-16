"""2017 - Day 4 Part 1: High-Entropy Passphrases."""

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
