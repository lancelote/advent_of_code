"""2015 - Day 17 Part 2: No Such Thing as Too Much."""

from src.year2015.day17a import process_data


def count_options(containers: list[int], target: int) -> int:
    combinations = 0
    min_n = len(containers)

    def dfs(i: int = 0, so_far: int = 0, n: int = 0) -> None:
        nonlocal combinations
        nonlocal min_n

        if so_far == target:
            if n < min_n:
                combinations = 1
                min_n = n

            elif n == min_n:
                combinations += 1

            return

        if so_far > target:
            return

        if i >= len(containers):
            return

        if n > min_n:
            return

        dfs(i + 1, so_far, n)
        dfs(i + 1, so_far + containers[i], n + 1)

    dfs()
    return combinations


def solve(task: str) -> int:
    containers = process_data(task)
    return count_options(containers, target=150)
