"""2016 - Day 6 Part 1: Signals and Noise."""
from collections import Counter


def process_data(data: str) -> list[tuple[str, ...]]:
    """Convert raw data into the list of tuples.

    Each tuple corresponds to one character.
    """
    lines = data.strip().split("\n")
    return list(zip(*lines))


def solve(task: str) -> str:
    """Filter errors from the message."""
    message = ""
    for char in process_data(task):
        message += Counter(char).most_common(1)[0][0]
    return message
