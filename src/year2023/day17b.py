"""2023 - Day 17 Part 2: Clumsy Crucible"""

from src.year2023.day17a import get_least_loss_path


def solve(task: str) -> int:
    city = [[int(x) for x in line] for line in task.splitlines()]
    return get_least_loss_path(city, min_path=4, max_path=10)
