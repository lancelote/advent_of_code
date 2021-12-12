"""2017 - Day 6 Part 2: Memory Reallocation.

Out of curiosity, the debugger would also like to know the size of the loop:
starting from a state that has already been seen, how many block
redistribution cycles must be performed before that same state is seen again?

In the example above, 2 4 1 2 is seen again after four cycles, and so the
answer in that example would be 4.

How many cycles are in the infinite loop that arises from the configuration
in your puzzle input?
"""
from typing import Dict

from src.year2017.day06a import Memory


def solve(task: str) -> int:
    """Find the distance between first duplicate bank distributions."""
    banks = [int(bank) for bank in task.strip().split()]
    memory = Memory(banks)
    seen: Dict[str, int] = {}
    index = 0

    while str(memory) not in seen:
        seen[str(memory)] = index
        memory.redistribute()
        index += 1

    return index - seen[str(memory)]
