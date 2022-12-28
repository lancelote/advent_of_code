"""2018 - Day 1 Part 2: Chronal Calibration."""
from itertools import cycle

from src.year2018.day01a import process_data


def solve(task: str) -> int:
    """Find first duplicate frequency."""
    current = 0
    seen = {current}
    for change in cycle(process_data(task)):
        current += change
        if current in seen:
            return current
        else:
            seen.add(current)
    return 0
