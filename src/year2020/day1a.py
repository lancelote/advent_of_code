"""2020 - Day 1 Part 1: Report Repair."""

from typing import List
from typing import Tuple


def process_data(data: str) -> List[int]:
    return [int(number) for number in data.strip().split("\n")]


def find_2020_summands(numbers: List[int]) -> Tuple[int, int]:
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            if numbers[i] + numbers[j] == 2020:
                return numbers[i], numbers[j]
    raise ValueError("no 2020 summands were found in input")


def solve(task: str) -> int:
    """Find two number which sum is 2020 and multiply them."""
    numbers = process_data(task)
    first, second = find_2020_summands(numbers)
    return first * second
