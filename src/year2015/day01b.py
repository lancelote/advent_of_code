"""2015 - Day 1 Part 2: Not Quite Lisp."""


def solve(task: str) -> int:
    level = 0

    for i, char in enumerate(task, start=1):
        if char == "(":
            level += 1
        elif char == ")":
            level -= 1
        if level == -1:
            return i

    raise ValueError("have never reached the basement")
