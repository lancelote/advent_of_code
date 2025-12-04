"""2025 - Day 3 Part 2: Lobby"""

from typing import Iterator

from src.year2025.day03a import process_data


def digit_generator(bank: list[int]) -> Iterator[int]:
    start = 0

    for count in range(12):
        candidate = bank[start]

        for i in range(start, len(bank) - (11 - count)):
            if bank[i] > candidate:
                candidate = bank[i]
                start = i

        yield candidate
        start += 1


def max_joltage(bank: list[int]) -> int:
    result = 0
    digits = digit_generator(bank)

    for _ in range(12):
        digit = next(digits)
        result *= 10
        result += digit

    return result


def solve(task: str) -> int:
    banks = process_data(task)
    return sum(max_joltage(bank) for bank in banks)
