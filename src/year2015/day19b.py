"""2015 - Day 19 Part 2: Medicine for Rudolph."""

from src.year2015.day19a import process_data
from src.year2015.day19a import tokenize


def count_steps(replacements: dict[str, list[str]], target: list[str]) -> int:
    visited: dict[str, int] = {}

    def dfs(current: list[str], so_far: int = 0) -> None:
        print(current)
        if len(current) > len(target):
            return

        key = "".join(current)
        if key in visited and visited[key] < so_far:
            return

        visited[key] = so_far

        for i, token in enumerate(current):
            if token in replacements:
                left = "".join(current[:i])
                right = "".join(current[i + 1 :])

                for replacement in replacements[token]:
                    mutation = left + replacement + right
                    dfs(tokenize(mutation), so_far + 1)

    dfs(["e"])
    return visited["".join(target)]


def solve(task: str) -> int:
    replacements, target = process_data(task)
    return count_steps(replacements, target)
