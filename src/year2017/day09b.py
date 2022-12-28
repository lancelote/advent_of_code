"""2017 - Day 9 Part 2: Stream Processing."""


def solve(task: str) -> int:
    """Count total group score."""
    garbage_chars = 0
    garbage = False
    escape = False

    for token in task.strip():
        if escape:
            escape = False
        elif token == ">":
            garbage = False
        elif token == "!":
            escape = True
        elif garbage:
            garbage_chars += 1
        elif token == "{":
            pass
        elif token == "}":
            pass
        elif token == "<":
            garbage = True
    return garbage_chars
