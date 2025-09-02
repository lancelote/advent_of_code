"""2015 - Day 8 Part 2: Matchsticks."""

from src.year2015.day08a import String
from src.year2015.day08a import process_data


def encode_len(string: String) -> int:
    result = 2  # for quotes

    for x in string.text:
        match x:
            case '"' | "\\":
                result += 2
            case _:
                result += 1

    return result


def solve(task: str) -> int:
    return sum(encode_len(x) - x.in_code for x in process_data(task))
