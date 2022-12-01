"""2020 - Day 9 Part 2: Encoding Error."""
from collections import deque
from typing import Deque
from typing import List

from src.year2020.day09a import first_invalid


def find_contagious_range(target: int, data: List[int]) -> Deque[int]:
    contagious_range: Deque[int] = deque()

    for number in data:
        contagious_range.append(number)

        while sum(contagious_range) > target:
            contagious_range.popleft()

        if sum(contagious_range) == target:
            return contagious_range

    raise ValueError("no contagious range was found")


def solve(task: str, preamble_length: int = 25) -> int:
    data = [int(num) for num in task.strip().split("\n")]
    invalid_number = first_invalid(data, preamble_length)
    contagious_range = find_contagious_range(invalid_number, data)
    return sum([min(contagious_range), max(contagious_range)])
