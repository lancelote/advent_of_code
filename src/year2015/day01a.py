"""2015 - Day 1 Part 1: Not Quite Lisp."""


def solve(task: str) -> int:
    return sum(1 if x == "(" else -1 for x in task)
