"""2019 - Day 4 Part 2: Secure Container.

An Elf just remembered one more important detail: the two adjacent matching
digits are not part of a larger group of matching digits.

Given this additional criterion, but still ignoring the range rule,
the following are now true:

    - 112233 meets these criteria because the digits never decrease and all
    repeated digits are exactly two digits long.
    - 123444 no longer meets the criteria (the repeated 44 is part of a larger
    group of 444).
    - 111122 meets the criteria (even though 1 is repeated more than twice, it
    still contains a double 22).

How many different passwords within the range given in your puzzle input meet
all of the criteria?
"""
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
