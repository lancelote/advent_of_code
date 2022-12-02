"""2015 - Day 3 Part 2: Perfectly Spherical Houses in a Vacuum."""
from src.year2015.day03a import visit_houses


def solve(task: str) -> int:
    """Solve the puzzle.

    Args:
        task (str): '>^<v...'

    Returns:
        int: Number of houses with at least one present

    """
    santa_task = task[0::2]
    robo_santa_task = task[1::2]
    visited_by_santa = visit_houses(santa_task)
    visited_by_robo = visit_houses(robo_santa_task)
    visited_by_santa.update(visited_by_robo)
    return len(visited_by_santa)
