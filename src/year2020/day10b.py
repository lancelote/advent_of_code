"""2020 - Day 10 Part 2: Adapter Array."""

from functools import lru_cache

from src.year2020.day10a import process_data


def solve(task: str) -> int:
    """Count possible arrangements"""

    @lru_cache
    def count_arrangements(i: int = 0) -> int:
        if i == len(adapters) - 1:
            return 1

        result = 0

        try:
            if adapters[i + 1] - adapters[i] <= 3:
                result += count_arrangements(i + 1)
            if adapters[i + 2] - adapters[i] <= 3:
                result += count_arrangements(i + 2)
            if adapters[i + 3] - adapters[i] <= 3:
                result += count_arrangements(i + 3)
        except IndexError:
            pass

        return result

    adapters: list[int] = process_data(task)
    adapters.append(0)
    adapters = sorted(adapters)
    return count_arrangements()
