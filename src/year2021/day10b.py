"""2021 - Day 10 Part 2: Syntax Scoring."""
from src.year2021.day10a import CLOSE
from src.year2021.day10a import MATCHING_CLOSE
from src.year2021.day10a import OPEN

POINTS = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}


def get_score(stack: list[str]) -> int:
    total = 0

    for ch in reversed(stack):
        total = total * 5 + POINTS[MATCHING_CLOSE[ch]]

    return total


def solve(task: str) -> int:
    subsystem: list[str] = task.split("\n")
    scores = []

    for line in subsystem:
        stack = []
        for ch in line:
            if ch in OPEN:
                stack.append(ch)
            elif ch in CLOSE:
                last = stack.pop()
                if MATCHING_CLOSE[last] != ch:
                    break  # skip corrupted
        else:
            scores.append(get_score(stack))

    return sorted(scores)[len(scores) // 2]
