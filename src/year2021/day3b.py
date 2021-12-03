from collections.abc import Callable
from typing import Iterator

from src.year2021.day3a import least_common
from src.year2021.day3a import most_common

Criteria = Callable[[str, int, Iterator[str]], bool]


def search(nums: list[str], criteria: Criteria) -> int:
    i_bit = 0
    left_indexes = set(range(len(nums)))

    while len(left_indexes) != 1:
        filtered_out = set()

        for i in left_indexes:
            left_nums = (nums[i] for i in left_indexes)
            if not criteria(nums[i], i_bit, left_nums):
                filtered_out.add(i)

        left_indexes.difference_update(filtered_out)
        i_bit += 1

    last_index_left = left_indexes.pop()
    return int(nums[last_index_left], base=2)


def oxygen_criteria(num: str, i_bit: int, nums: Iterator[str]) -> bool:
    i_bits = (num[i_bit] for num in nums)
    return num[i_bit] == most_common(i_bits)


def co2_criteria(num: str, i_bit: int, nums: Iterator[str]) -> bool:
    i_bits = (num[i_bit] for num in nums)
    return num[i_bit] == least_common(i_bits)


def solve(task: str) -> int:
    nums = [x for x in task.strip().split("\n")]

    oxygen = search(nums, oxygen_criteria)
    co2 = search(nums, co2_criteria)

    return oxygen * co2
