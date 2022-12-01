"""2022 - Day 1 Part 2: Calorie Counting."""

import heapq
from src.year2022.day01a import process_data


def solve(task: str) -> int:
    heap: list[int] = []
    elves = process_data(task)

    for elf in elves:
        heapq.heappush(heap, elf)
        if len(heap) > 3:
            heapq.heappop(heap)

    return sum(heap)
