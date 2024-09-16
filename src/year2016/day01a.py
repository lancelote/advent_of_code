"""2016 - Day 1 Part 1: No Time for a Taxicab."""

from collections import namedtuple
from typing import Any

Instruction = namedtuple("Instruction", "direction distance")


class Point:
    """Point coordinates representation."""

    def __init__(self, x: int = 0, y: int = 0) -> None:
        """2D point representation.

        Args:
            x (int): x coordinates
            y (int): y coordinates

        """
        self.x = x
        self.y = y

    def move(self, direction: int, distance: int) -> None:
        """Move the point to given direction by given distance."""
        if direction == 0:  # North
            self.y += distance
        elif direction == 1:  # East
            self.x += distance
        elif direction == 2:  # South
            self.y -= distance
        elif direction == 3:  # West
            self.x -= distance

    def distance_from_zero(self) -> int:
        """Compute squared city distance from (0, 0) to the point."""
        return abs(self.x) + abs(self.y)

    def __repr__(self) -> str:
        """Point(1, 2) -> (1, 2)."""
        return f"({self.x}, {self.y})"

    def __eq__(self, other: Any) -> bool:
        """Check if the two Point equal (have the same coordinates)."""
        assert isinstance(other, Point)
        return self.x == other.x and self.y == other.y


def processed_data(data: str) -> list[Instruction]:
    """Convert raw sequence of instructions into the list of named tuples."""
    return [Instruction(x[0], int(x[1:])) for x in data.split(", ")]


def update_direction(direction: int, turn: str) -> int:
    """Return the directions ID after the given turn."""
    answer = 0
    if turn == "R":
        answer = (direction + 1) % 4
    elif turn == "L":
        answer = (direction - 1) % 4
    return answer


def solve(task: str) -> int:
    """Compute how many blocks away is Easter Bunny HQ."""
    direction = 0  # North
    current = Point()
    instructions = processed_data(task)

    for instruction in instructions:
        direction = update_direction(direction, instruction.direction)
        current.move(direction, instruction.distance)
    return current.distance_from_zero()
