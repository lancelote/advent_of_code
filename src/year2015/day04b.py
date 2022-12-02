"""2015 - Day 4 Part 2: The Ideal Stocking Stuffer."""
from src.year2015.day04a import solve as part_a_solve


def solve(task: str) -> int:
    """Solve the puzzle.

    Args:
        task (str): key to encode

    Returns:
        int: Biggest number

    """
    return part_a_solve(task, zeros=6)
