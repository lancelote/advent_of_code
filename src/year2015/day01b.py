"""2015 - Day 1 Part 2: Not Quite Lisp."""


def solve(task: str) -> int:
    """Solve puzzle.

    Args:
        task (str): Puzzle input

    Returns:
        int: Puzzle solution

    """
    answer = 0
    level = 0
    i = 0
    for char in task:
        i += 1
        if char == "(":
            level += 1
        elif char == ")":
            level -= 1
        if level == -1:
            answer = i
            break
    return answer
