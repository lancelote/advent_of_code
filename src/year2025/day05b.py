"""2025 - Day 5 Part 2: Cafeteria"""

from src.year2025.day05a import process_data


def solve(task: str) -> int:
    ranges, _ = process_data(task)
    ranges.sort()

    count = 0
    left, right = ranges[0]

    for li, ri in ranges:
        if li > right:
            count += right - left + 1
            left = li

        if ri > right:
            right = ri

    count += right - left + 1
    return count
