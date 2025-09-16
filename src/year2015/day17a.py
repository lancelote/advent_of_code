"""2015 - Day 17 Part 1: No Such Thing as Too Much."""


def process_data(data: str) -> list[int]:
    return [int(x) for x in data.splitlines()]


def count_options(containers: list[int], target: int) -> int:
    combinations = 0

    def dfs(i: int = 0, so_far: int = 0) -> None:
        nonlocal combinations

        if so_far == target:
            combinations += 1
            return

        if so_far > target:
            return

        if i >= len(containers):
            return

        dfs(i + 1, so_far)
        dfs(i + 1, so_far + containers[i])

    dfs()
    return combinations


def solve(task: str) -> int:
    containers = process_data(task)
    return count_options(containers, target=150)
