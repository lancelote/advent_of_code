"""2021 - Day 3 Part 1: Binary Diagnostic."""

from collections.abc import Iterator


def count_zeros_and_ones(bits: Iterator[str]) -> tuple[int, int]:
    zeros = 0
    ones = 0

    for bit in bits:
        if bit == "0":
            zeros += 1
        else:
            ones += 1

    return zeros, ones


def most_common(bits: Iterator[str]) -> str:
    zeros, ones = count_zeros_and_ones(bits)
    return "0" if zeros > ones else "1"


def least_common(bits: Iterator[str]) -> str:
    zeros, ones = count_zeros_and_ones(bits)
    return "0" if zeros <= ones else "1"


def iterate_bits(nums: list[str]) -> Iterator[Iterator[str]]:
    bits_in_num = len(nums[0])

    for i in range(bits_in_num):
        yield (num[i] for num in nums)


def get_gamma(nums: list[str]) -> int:
    result = []

    for i_bits in iterate_bits(nums):
        result.append(most_common(i_bits))

    return int("".join(result), base=2)


def get_epsilon(nums: list[str]) -> int:
    result = []

    for i_bits in iterate_bits(nums):
        result.append(least_common(i_bits))

    return int("".join(result), base=2)


def solve(task: str) -> int:
    nums = task.strip().split("\n")

    gamma = get_gamma(nums)
    epsilon = get_epsilon(nums)

    return gamma * epsilon
