"""2019 - Day 4 Part 1: Secure Container."""
from collections.abc import Iterator

Password = Iterator[str]


def two_adjacent(num: str) -> bool:
    """Check for at least two equal adjacent digits."""
    return any(num[i] == num[i - 1] for i in range(1, len(num)))


def never_decrease(num: str) -> bool:
    """Check if digits are never decrease."""
    return all(int(num[i]) >= int(num[i - 1]) for i in range(1, len(num)))


def process_data(data: str) -> Iterator[int]:
    """Process initial data."""
    return map(int, data.strip().split("-"))


def get_passwords(start: int, stop: int) -> Password:
    """Get all possible passwords."""
    return map(str, range(start, stop))


def solve(task: str) -> int:
    """Count the number of possible passwords."""
    start, stop = process_data(task)
    return len(
        [
            password
            for password in get_passwords(start, stop)
            if two_adjacent(password) and never_decrease(password)
        ]
    )
