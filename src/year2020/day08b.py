"""2020 - Day 8 Part 1: Handheld Halting."""
from typing import List

from src.year2020.day08a import Instruction
from src.year2020.day08a import process_data
from src.year2020.day08a import run


def attempt(instructions: List[Instruction]) -> int:
    for instruction in instructions:
        if instruction.is_swapable:
            instruction.swap()
            graceful, acc = run(instructions)
            if graceful:
                return acc
            instruction.swap()

    raise ValueError("corrupted operation was not found")


def solve(task: str) -> int:
    """What is the value of accumulator after termination?"""
    instructions = process_data(task)
    return attempt(instructions)
