"""2017 - Day 4 Part 2: High-Entropy Passphrases.

For added security, yet another system policy has been put in place. Now, a
valid passphrase must contain no two words that are anagrams of each other -
that is, a passphrase is invalid if any word's letters can be rearranged to
form any other word in the passphrase.

For example:

    - "abcde fghij" is a valid passphrase.
    - "abcde xyz ecdab" is not valid - the letters from the third word can be
      rearranged to form the first word.
    - "a ab abc abd abf abj" is a valid passphrase, because all letters need to
      be used when forming another word.
    - "iiii oiii ooii oooi oooo" is valid.
    - "oiii ioii iioi iiio" is not valid - any of these words can be rearranged
      to form any other word.

Under this new system policy, how many passphrases are valid?
"""
from src.year2017.day4a import count_valid


def anagrams(passphrase: str) -> bool:
    """Check if there are anagrams in passphrase."""
    words = passphrase.split()
    return len(words) == len({"".join(sorted(word)) for word in words})


def solve(task: str) -> int:
    """Count number of passphrases without anagrams."""
    return count_valid(task, valid=anagrams)
