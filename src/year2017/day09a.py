"""2017 - Day 9 Part 1: Stream Processing."""


def solve(task: str) -> int:
    """Count total group score."""
    score = 0
    total = 0
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
            pass
        elif token == "{":
            score += 1
            total += score
        elif token == "}":
            score -= 1
        elif token == "<":
            garbage = True
    return total
