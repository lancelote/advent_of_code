"""2020 - Day 5 Part 2: Binary Boarding."""
from src.year2020.day5a import process_data


def solve(task: str) -> int:
    """Find an empty seat."""
    seats = process_data(task)
    first = min(seats).pk
    last = max(seats).pk

    ideal = set(range(first, last))
    real = set(seat.pk for seat in seats)
    difference = ideal.difference(real)
    assert len(difference), "difference is not a single seat"

    return difference.pop()
