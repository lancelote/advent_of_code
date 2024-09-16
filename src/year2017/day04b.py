"""2017 - Day 4 Part 2: High-Entropy Passphrases."""

from src.year2017.day04a import count_valid


def anagrams(passphrase: str) -> bool:
    """Check if there are anagrams in passphrase."""
    words = passphrase.split()
    return len(words) == len({"".join(sorted(word)) for word in words})


def solve(task: str) -> int:
    """Count number of passphrases without anagrams."""
    return count_valid(task, valid=anagrams)
