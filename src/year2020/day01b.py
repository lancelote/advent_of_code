"""2020 - Day 1 Part 1: Report Repair."""

from src.year2020.day01a import process_data


def find_three_2020_summands(numbers: list[int]) -> tuple[int, int, int]:
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            for k in range(j, len(numbers)):
                if numbers[i] + numbers[j] + numbers[k] == 2020:
                    return numbers[i], numbers[j], numbers[k]
    raise ValueError("no 2020 summands were found in input")


def solve(task: str) -> int:
    """Find two number which sum is 2020 and multiply them."""
    numbers = process_data(task)
    first, second, third = find_three_2020_summands(numbers)
    return first * second * third
