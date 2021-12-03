from typing import Iterator


def count_zeros_and_ones(bits: Iterator[str]) -> tuple[int, int]:
    zeros = 0
    ones = 0

    for bit in bits:
        if bit == "0":
            zeros += 1
        else:
            ones += 1

    return zeros, ones


def get_most_common(bits: Iterator[str]) -> str:
    zeros, ones = count_zeros_and_ones(bits)
    return "0" if zeros > ones else "1"


def get_least_common(bits: Iterator[str]) -> str:
    zeros, ones = count_zeros_and_ones(bits)
    return "0" if zeros <= ones else "1"


def iterate_bits(nums: list[str]) -> Iterator[Iterator[str]]:
    bits_in_num = len(nums[0])

    for i in range(bits_in_num):
        yield (num[i] for num in nums)


def get_gamma(nums: list[str]) -> int:
    result = []

    for i_bits in iterate_bits(nums):
        result.append(get_most_common(i_bits))

    return int("".join(result), base=2)


def get_epsilon(nums: list[str]) -> int:
    result = []

    for bits in iterate_bits(nums):
        result.append(get_least_common(bits))

    return int("".join(result), base=2)


def solve(task: str) -> int:
    nums = [x for x in task.strip().split("\n")]

    gamma = get_gamma(nums)
    epsilon = get_epsilon(nums)

    return gamma * epsilon
