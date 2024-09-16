"""2022 - Day 7 Part 2: No Space Left On Device."""

from src.year2022.day07a import count_size
from src.year2022.day07a import process_data


def solve(task: str) -> int:
    total = 70_000_000
    required = 30_000_000

    root = process_data(task)
    cache: dict[str, int] = {}
    count_size(root, cache)

    used = cache["/"]

    for x in sorted(cache.values()):
        if total - used + x >= required:
            return x

    raise ValueError("no big enough directory found")
