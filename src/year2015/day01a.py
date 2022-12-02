"""2015 - Day 1 Part 1: Not Quite Lisp."""


def solve(task: str) -> int:
    return task.count("(") - task.count(")")
