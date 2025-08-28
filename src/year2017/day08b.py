"""2017 - Day 8 Part 2: I Heard You Like Registers."""

from src.year2017.day08a import perform_instructions, process_data


def solve(task: str) -> int:
    """Find the biggest register value seen."""
    instructions = process_data(task)
    _, biggest = perform_instructions(instructions)
    return biggest
