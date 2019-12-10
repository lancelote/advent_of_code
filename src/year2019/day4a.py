"""2019 - Day 4 Part 1: Secure Container.

You arrive at the Venus fuel depot only to discover it's protected by a
password. The Elves had written the password on a sticky note, but someone
threw it out.

However, they do remember a few key facts about the password:

    - It is a six-digit number.
    - The value is within the range given in your puzzle input.
    - Two adjacent digits are the same (like 22 in 122345).
    - Going from left to right, the digits never decrease; they only ever
      increase or stay the same (like 111123 or 135679).

Other than the range rule, the following are true:

    - 111111 meets these criteria (double 11, never decreases).
    - 223450 does not meet these criteria (decreasing pair of digits 50).
    - 123789 does not meet these criteria (no double).

How many different passwords within the range given in your puzzle input meet
these criteria?
"""

from typing import Generator


def two_next(num: int) -> bool:
    """Check for at least two equal adjacent digits."""
    pas = str(num)
    return any(pas[i] == pas[i - 1] for i in range(1, len(pas)))


def not_decrease(num: int) -> bool:
    """Check if digits are never decrease."""
    pas = str(num)
    return all(int(pas[i]) >= int(pas[i - 1]) for i in range(1, len(pas)))


def process_data(data: str):
    """Process initial data."""
    return map(int, data.strip().split('-'))


def get_passwords(start: int, stop: int) -> Generator[int, None, None]:
    """Get all possible passwords."""
    return (p for p in range(start, stop) if two_next(p) and not_decrease(p))


def solve(task: str) -> int:
    """Count the number of possible passwords."""
    return len(list(get_passwords(*process_data(task))))
