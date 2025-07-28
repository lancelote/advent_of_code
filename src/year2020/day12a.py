"""2020 - Day 12 Part 1: Rain Risk."""

from __future__ import annotations

import re
from enum import Enum
from typing import NamedTuple
from typing import assert_never


class Direction(Enum):
    NORTH = "N"
    SOUTH = "S"
    EAST = "E"
    WEST = "W"
    LEFT = "L"
    RIGHT = "R"
    FORWARD = "F"


CARTESIAN = [Direction.NORTH, Direction.EAST, Direction.SOUTH, Direction.WEST]


class Instruction(NamedTuple):
    direction: Direction
    value: int

    @classmethod
    def from_line(cls, line: str) -> Instruction:
        [(direction, value)] = re.findall(r"^(\w)(\d+)$", line)
        return cls(Direction(direction), int(value))


class Ship:
    def __init__(self, direction: Direction = Direction.EAST):
        self.direction = direction
        self.x = 0
        self.y = 0

    def apply_instructions(self, instructions: list[Instruction]) -> None:
        for instruction in instructions:
            self.apply_instruction(instruction)

    def turn(self, angle: int) -> None:
        current_index = CARTESIAN.index(self.direction)
        shift = int(angle / 90)
        self.direction = CARTESIAN[(current_index + shift) % 4]

    def apply_instruction(self, instruction: Instruction) -> None:
        if instruction.direction is Direction.NORTH:
            self.y += instruction.value
        elif instruction.direction is Direction.SOUTH:
            self.y -= instruction.value
        elif instruction.direction is Direction.EAST:
            self.x += instruction.value
        elif instruction.direction is Direction.WEST:
            self.x -= instruction.value
        elif instruction.direction is Direction.LEFT:
            self.turn(-instruction.value)
        elif instruction.direction is Direction.RIGHT:
            self.turn(instruction.value)
        elif instruction.direction is Direction.FORWARD:
            self.apply_instruction(
                Instruction(self.direction, instruction.value)
            )
        else:
            assert_never(instruction.direction)

    @property
    def manhattan_distance(self) -> int:
        return abs(self.x) + abs(self.y)


def process_data(data: str) -> list[Instruction]:
    return [Instruction.from_line(line) for line in data.strip().split("\n")]


def solve(task: str) -> int:
    """Find the Manhattan distance to ship."""
    ship = Ship()
    instructions = process_data(task)
    ship.apply_instructions(instructions)
    return ship.manhattan_distance
