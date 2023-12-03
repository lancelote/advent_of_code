"""2023 - Day 3 Part 2: Gear Ratios"""
from collections import defaultdict

from src.year2023.day03a import process_data


def solve(task: str) -> int:
    total = 0
    parts = process_data(task)
    symbols: dict[tuple[int, int], list[int]] = defaultdict(list)

    for part in parts:
        if part.symbol.value == "*":
            symbols[part.symbol.coords].append(part.number)

    for connected in symbols.values():
        if len(connected) == 2:
            x, y = connected
            gear_ratio = x * y
            total += gear_ratio

    return total
