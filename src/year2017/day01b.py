"""2017 - Day 1 Part 2: Inverse Captcha."""


def solve(task: str) -> int:
    """Sum all digits that match the halfway around digit in the list."""
    result = 0
    task = task.strip()
    shift = len(task) // 2

    for i, digit in enumerate(task):
        if digit == task[(i + shift) % len(task)]:
            result += int(digit)
    return result
