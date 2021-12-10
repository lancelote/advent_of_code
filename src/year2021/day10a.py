"""2021 - Day 10 Part 1: Syntax Scoring."""

POINTS = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

OPEN = {"(", "[", "{", "<"}
CLOSE = {")", "]", "}", ">"}

MATCHING_CLOSE = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}


def solve(task: str) -> int:
    subsystem: list[str] = task.split("\n")
    score = 0

    for line in subsystem:
        stack = []
        for ch in line:
            if ch in OPEN:
                stack.append(ch)
            elif ch in CLOSE:
                last = stack.pop()
                if MATCHING_CLOSE[last] != ch:
                    score += POINTS[ch]

    return score
