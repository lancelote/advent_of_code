"""2016 - Day 6 Part 1: Signals and Noise."""

from collections import Counter

from src.year2016.day06a import process_data


def solve(task: str) -> str:
    """Filter errors from the message."""
    message = ""
    for char in process_data(task):
        message += Counter(char).most_common()[-1][0]
    return message
