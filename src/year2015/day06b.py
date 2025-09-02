"""2015 - Day 6 Part 1: Probably a Fire Hazard."""

from src.year2015.day06a import Command
from src.year2015.day06a import compute_result


def update_light(command: Command, light: int) -> int:
    logic = {
        "toggle": light + 2,
        "turn on": light + 1,
        "turn off": max(0, light - 1),
    }
    return logic[command]


def solve(task: str) -> int:
    return compute_result(task, update_light)
