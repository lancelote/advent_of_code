"""2015 - Day 6 Part 1: Probably a Fire Hazard."""

import enum
import re
from collections.abc import Callable
from typing import NamedTuple

PATTERN = re.compile(r"([a-z ]*) ([\d,]*) through ([\d,]*)")


class Command(enum.StrEnum):
    TURN_ON = "turn on"
    TURN_OFF = "turn off"
    TOGGLE = "toggle"


class Coordinates(NamedTuple):
    x: int
    y: int


class Instruction(NamedTuple):
    command: Command
    start: Coordinates
    end: Coordinates


def process_data(data: str) -> list[Instruction]:
    processed_data = []

    for string in data.strip().split("\n"):
        match = re.match(PATTERN, string)
        assert match

        command, start, end = match.groups()
        start = Coordinates(*map(int, start.split(",")))
        end = Coordinates(*map(int, end.split(",")))
        processed_data.append(Instruction(Command(command), start, end))

    return processed_data


def update_light(command: Command, light: int) -> int:
    logic = {
        Command.TOGGLE: int(not light),
        Command.TURN_ON: 1,
        Command.TURN_OFF: 0,
    }
    return logic[command]


def compute_result(task: str, execute: Callable[[Command, int], int]) -> int:
    instructions = process_data(task)
    lights = [[0] * 1000 for _ in range(1000)]

    for instruction in instructions:
        for i in range(instruction.start.x, instruction.end.x + 1):
            for j in range(instruction.start.y, instruction.end.y + 1):
                lights[i][j] = execute(instruction.command, lights[i][j])

    return sum(light for row in lights for light in row)


def solve(task: str) -> int:
    return compute_result(task, update_light)
