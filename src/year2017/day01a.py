"""2017 - Day 1 Part 1: Inverse Captcha."""


def solve(task: str) -> int:
    """Sum all digits that match the next digit in the list."""
    result = 0
    task = task.strip()
    for i, digit in enumerate(task):
        if digit == task[i - 1]:
            result += int(digit)
    return result
