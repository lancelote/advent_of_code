"""2017 - Day 6 Part 2: Memory Reallocation."""
from src.year2017.day06a import Memory


def solve(task: str) -> int:
    """Find the distance between first duplicate bank distributions."""
    banks = [int(bank) for bank in task.strip().split()]
    memory = Memory(banks)
    seen: dict[str, int] = {}
    index = 0

    while str(memory) not in seen:
        seen[str(memory)] = index
        memory.redistribute()
        index += 1

    return index - seen[str(memory)]
