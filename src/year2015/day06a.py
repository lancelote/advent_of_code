"""2015 - Day 6 Part 1: Probably a Fire Hazard."""

import re
from collections import namedtuple
from collections.abc import Callable

PATTERN = re.compile(r"([a-z ]*) ([\d,]*) through ([\d,]*)")

Coordinates = namedtuple("Coordinates", ["x", "y"])
Instruction = namedtuple("Instruction", ["command", "start", "end"])


def process_data(data: str) -> list[Instruction]:
    r"""Process row data into list of namedtuples.

    Args:
        data (str): turn on 489,959 through 759,964\n...

    Returns:
        lst: [namedtuple(command, start, end), ...] where start and end are
            coordinates namedtuple(x, y)

    """
    processed_data = []

    for string in data.strip().split("\n"):
        match = re.match(PATTERN, string)
        assert match

        command, start, end = match.groups()
        start = Coordinates(*map(int, start.split(",")))
        end = Coordinates(*map(int, end.split(",")))
        processed_data.append(Instruction(command, start, end))

    return processed_data


def update_light(command: str, light: int) -> int:
    """Compute new light status.

    Args:
        command (str): 'toggle', 'turn on' or 'turn off'
        light (int): Light status before command execution

    Returns:
        bool: New light status

    """
    logic = {"toggle": not light, "turn on": 1, "turn off": 0}
    return logic[command]


def compute_result(task: str, execute: Callable[[str, int], int]) -> int:
    r"""Calculate number of powered lights after all instructions.

    Args:
        execute: Function which returns new light status after given command
            and previous light status
        task (str): turn on 489,959 through 759,964\n...

    Returns:
        int: Number of powered lights

    """
    instructions = process_data(task)
    lights = [[0] * 1000 for _ in range(1000)]

    for instruction in instructions:
        for i in range(instruction.start.x, instruction.end.x + 1):
            for j in range(instruction.start.y, instruction.end.y + 1):
                lights[i][j] = execute(instruction.command, lights[i][j])

    return sum(light for row in lights for light in row)


def solve(task: str) -> int:
    r"""Calculate number of powered lights after all instructions.

    Args:
        task (str): turn on 489,959 through 759,964\n...

    Returns:
        int: Number of powered lights

    """
    return compute_result(task, update_light)
