"""2018 - Day 2 Part 1: Inventory Management System."""
from collections import Counter
from collections.abc import Iterator


def process_data(data: str) -> Iterator[Counter[str]]:
    """Create stream of counters for each input line."""
    for box in data.strip().split("\n"):
        yield Counter(box)


def solve(task: str) -> int:
    """Calculate input checksum."""
    twos = 0
    threes = 0
    for box in process_data(task):
        if 2 in box.values():
            twos += 1
        if 3 in box.values():
            threes += 1
    return twos * threes
