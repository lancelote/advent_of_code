"""2015 - Day 5 Part 2: Doesn't He Have Intern-Elves For This."""

import re

from src.year2015.day05a import process_data


def is_nice(word: str) -> bool:
    """Check if string is nice.

    Args:
        word: String to check

    Returns:
        bool: True if nice, False if naughty

    """
    pairs = len(re.findall(r"(..).*\1", word))
    guarded_letter = len(re.findall(r"(.).\1", word))
    return pairs >= 1 and guarded_letter >= 1


def solve(task: str) -> int:
    r"""Calculate number of nice strings.

    Args:
        task (str): agagasdgsdg \n aasdfasgsdg \n ... (without spaces)

    Returns:
        int: Number of nice strings

    """
    data = process_data(task)
    return sum(is_nice(line) for line in data)
