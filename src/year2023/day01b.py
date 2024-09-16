"""2023 - Day 1 Part 2: Trebuchet?!"""

import re

from src.year2023.day01a import process_data

TO_DIGIT = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def get_num(line: str) -> int:
    pattern = r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))"
    match = re.findall(pattern, line)

    first = match[0]
    last = match[-1]

    first = first if first.isdigit() else TO_DIGIT[first]
    last = last if last.isdigit() else TO_DIGIT[last]

    return int(first + last)


def solve(task: str) -> int:
    return sum(get_num(line) for line in process_data(task))
