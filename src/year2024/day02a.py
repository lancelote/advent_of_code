"""2024 - Day 2 Part 1: Red-Nosed Reports"""


def is_increasing(level: list[int]) -> bool:
    for i in range(len(level) - 1):
        if level[i] > level[i + 1]:
            return False
    return True


def is_decreasing(level: list[int]) -> bool:
    for i in range(len(level) - 1):
        if level[i] < level[i + 1]:
            return False
    return True


def ok_diff(level: list[int]) -> bool:
    for i in range(len(level) - 1):
        diff = abs(level[i] - level[i + 1])
        if diff < 1 or diff > 3:
            return False
    return True


def is_safe(level: list[int]) -> bool:
    return (is_increasing(level) or is_decreasing(level)) and ok_diff(level)


def solve(task: str) -> int:
    lines = task.split("\n")
    levels = [[int(x) for x in line.split()] for line in lines]
    return sum(is_safe(level) for level in levels)
