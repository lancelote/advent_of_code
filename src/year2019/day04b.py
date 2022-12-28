"""2019 - Day 4 Part 2: Secure Container."""
import re

from src.year2019.day04a import get_passwords
from src.year2019.day04a import never_decrease
from src.year2019.day04a import process_data


def at_least_one_equal_pair(num: str) -> bool:
    """Check if at least one unique pair is present."""
    return any(len(group[0]) == 2 for group in re.findall(r"((.)\2+)", num))


def solve(task: str) -> int:
    """Count the number of possible passwords."""
    start, stop = process_data(task)
    return len(
        [
            password
            for password in get_passwords(start, stop)
            if all(
                [
                    at_least_one_equal_pair(password),
                    never_decrease(password),
                ]
            )
        ]
    )
