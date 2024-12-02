"""2024 - Day 2 Part 2: Red-Nosed Reports"""


def is_increasing(level: list[int], skip: bool = True) -> bool:
    for i in range(len(level) - 1):
        if not (1 <= level[i + 1] - level[i] <= 3):
            if not skip:
                return False
            left = is_increasing(level[:i] + level[i + 1 :], False)
            right = is_increasing(level[: i + 1] + level[i + 2 :], False)
            return left or right
    return True


def is_decreasing(level: list[int], skip: bool = True) -> bool:
    for i in range(len(level) - 1):
        if not (1 <= level[i] - level[i + 1] <= 3):
            if not skip:
                return False
            left = is_decreasing(level[:i] + level[i + 1 :], False)
            right = is_decreasing(level[: i + 1] + level[i + 2 :], False)
            return left or right
    return True


def is_safe(level: list[int]) -> bool:
    return is_increasing(level) or is_decreasing(level)


def solve(task: str) -> int:
    lines = task.split("\n")
    levels = [[int(x) for x in line.split()] for line in lines]
    return sum(is_safe(level) for level in levels)
