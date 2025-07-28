"""2020 - Day 12 Part 2: Rain Risk."""

from __future__ import annotations

from typing import assert_never

from src.year2020.day12a import Direction
from src.year2020.day12a import Instruction
from src.year2020.day12a import Ship
from src.year2020.day12a import process_data


class Waypoint:
    def __init__(self) -> None:
        # coordinates are based on the ship as (0, 0)
        self.x = 10
        self.y = 1


class ShipWithWaypoint(Ship):
    def __init__(self) -> None:
        super().__init__()
        self.wp = Waypoint()

    def turn(self, angle: int) -> None:
        if angle == 90 or angle == -270:
            self.wp.x, self.wp.y = self.wp.y, -self.wp.x
        elif angle == -90 or angle == 270:
            self.wp.x, self.wp.y = -self.wp.y, self.wp.x
        elif angle == 180 or angle == -180:
            self.wp.x, self.wp.y = -self.wp.x, -self.wp.y
        else:
            raise ValueError(f"unexpected angle: ${angle}")

    def move(self, times: int) -> None:
        self.x += self.wp.x * times
        self.y += self.wp.y * times

    def apply_instruction(self, instruction: Instruction) -> None:
        if instruction.direction is Direction.NORTH:
            self.wp.y += instruction.value
        elif instruction.direction is Direction.SOUTH:
            self.wp.y -= instruction.value
        elif instruction.direction is Direction.EAST:
            self.wp.x += instruction.value
        elif instruction.direction is Direction.WEST:
            self.wp.x -= instruction.value
        elif instruction.direction is Direction.LEFT:
            self.turn(-instruction.value)
        elif instruction.direction is Direction.RIGHT:
            self.turn(instruction.value)
        elif instruction.direction is Direction.FORWARD:
            self.move(instruction.value)
        else:
            assert_never(instruction.direction)


def solve(task: str) -> int:
    """Find the Manhattan distance to ship."""
    ship = ShipWithWaypoint()
    instructions = process_data(task)
    ship.apply_instructions(instructions)
    return ship.manhattan_distance
