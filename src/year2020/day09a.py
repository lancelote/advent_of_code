"""2020 - Day 9 Part 1: Encoding Error."""
from collections import deque
from itertools import combinations
from typing import Deque


def is_valid(num: int, preamble: Deque[int]) -> bool:
    for pair in combinations(preamble, 2):
        if sum(pair) == num:
            return True
    return False


def first_invalid(data: list[int], preamble_length: int) -> int:
    preamble = deque(data[:preamble_length])
    numbers = data[preamble_length:]

    for number in numbers:
        if is_valid(number, preamble):
            preamble.popleft()
            preamble.append(number)
        else:
            return number

    raise ValueError("invalid number was not found")


def solve(task: str, preamble_length: int = 25) -> int:
    """What is the first invalid number?"""
    data = [int(num) for num in task.strip().split("\n")]
    return first_invalid(data, preamble_length)
