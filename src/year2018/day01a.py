"""2018 - Day 1 Part 1: Chronal Calibration."""
from collections.abc import Generator


def process_data(data: str) -> Generator[int, None, None]:
    """Process frequency data yielding each change as integer."""
    for change in data.strip().split("\n"):
        yield int(change)


def solve(task: str) -> int:
    """Sum all frequency changes."""
    return sum(process_data(task))
