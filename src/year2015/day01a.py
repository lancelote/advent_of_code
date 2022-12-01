"""2015 - Day 1 Part 1: Not Quite Lisp."""


def solve(task: str) -> int:
    """Solve puzzle.

    Args:
        task (str): Puzzle input

    Returns:
        int: Puzzle solution

    """
    return task.count("(") - task.count(")")
