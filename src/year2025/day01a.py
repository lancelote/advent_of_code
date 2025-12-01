"""2025 - Day 1 Part 1: Secret Entrance"""

from dataclasses import dataclass
from enum import StrEnum


class Direction(StrEnum):
    L = "L"
    R = "R"


type Distance = int


@dataclass
class Rotation:
    direction: Direction
    distance: Distance

    @classmethod
    def from_line(cls, line) -> Rotation:
        return Rotation(Direction(line[0]), int(line[1:]))


def get_password(rotations: list[Rotation]) -> int:
    zero_count = 0
    dial = 50

    for rotation in rotations:
        shift = rotation.distance

        if rotation.direction is Direction.L:
            shift *= -1

        dial = (dial + shift) % 100
        if dial == 0:
            zero_count += 1

    return zero_count


def process_data(task: str) -> list[Rotation]:
    return [Rotation.from_line(line) for line in task.splitlines()]


def solve(task: str) -> int:
    rotations = process_data(task)
    return get_password(rotations)
