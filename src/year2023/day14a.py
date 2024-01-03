"""2023 - Day 14 Part 1: Parabolic Reflector Dish"""
from typing import TypeAlias

Platform: TypeAlias = list[list[str]]


def tilt_north(platform: Platform) -> None:
    rows = len(platform)
    cols = len(platform[0])

    for c in range(cols):
        last_empty_r = 0

        for r in range(rows):
            if platform[r][c] == "O":
                if r != last_empty_r:
                    platform[last_empty_r][c] = "O"
                    platform[r][c] = "."
                    last_empty_r += 1
                else:
                    last_empty_r += 1

            if platform[r][c] == "#":
                last_empty_r = r + 1


def count_load(platform: Platform) -> int:
    load = 0
    rows = len(platform)
    cols = len(platform[0])

    for r in range(rows):
        for c in range(cols):
            if platform[r][c] == "O":
                load += rows - r

    return load


def solve(task: str) -> int:
    platform = [list(line) for line in task.splitlines()]
    tilt_north(platform)
    return count_load(platform)
