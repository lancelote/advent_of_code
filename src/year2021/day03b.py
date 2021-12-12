"""2021 - Day 3 Part 2: Binary Diagnostic."""
from collections.abc import Callable
from typing import Iterator

from src.year2021.day03a import least_common
from src.year2021.day03a import most_common

Criteria = Callable[[str, int, Iterator[str]], bool]


def search(nums: list[str], criteria: Criteria) -> int:
    bit_index = 0
    left_indexes = set(range(len(nums)))

    while len(left_indexes) != 1:
        filtered_out = set()

        for left_index in left_indexes:
            left_nums = (nums[i] for i in left_indexes)
            num_to_check = nums[left_index]

            if not criteria(num_to_check, bit_index, left_nums):
                filtered_out.add(left_index)

        left_indexes.difference_update(filtered_out)
        bit_index += 1

    last_index_left = left_indexes.pop()
    return int(nums[last_index_left], base=2)


def oxygen_criteria(num: str, bit_index: int, nums: Iterator[str]) -> bool:
    i_bits = (num[bit_index] for num in nums)
    return num[bit_index] == most_common(i_bits)


def co2_criteria(num: str, bit_index: int, nums: Iterator[str]) -> bool:
    i_bits = (num[bit_index] for num in nums)
    return num[bit_index] == least_common(i_bits)


def solve(task: str) -> int:
    nums = task.strip().split("\n")

    oxygen = search(nums, oxygen_criteria)
    co2 = search(nums, co2_criteria)

    return oxygen * co2
