"""2017 - Day 8 Part 2: I Heard You Like Registers.

To be safe, the CPU also needs to know the highest value held in any register
during this process so that it can decide how much memory to allocate to these
operations. For example, in the above instructions, the highest value ever
held was 10 (in register c after the third instruction was evaluated).
"""

from src.year2017.day8a import process_data, perform_instructions


def solve(task: str) -> int:
    """Find the biggest register value seen."""
    instructions = process_data(task)
    _, biggest = perform_instructions(instructions)
    return biggest
