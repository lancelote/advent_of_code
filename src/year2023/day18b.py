"""2023 - Day 18 Part 2: Lavaduct Lagoon"""
from dataclasses import dataclass
from enum import Enum
from typing import Self
from typing import TypeAlias

Corner: TypeAlias = tuple[int, int]


class Direction(Enum):
    U = "3"
    R = "0"
    D = "1"
    L = "2"


SHIFTS = {
    Direction.U: (-1, 0),
    Direction.R: (0, +1),
    Direction.D: (+1, 0),
    Direction.L: (0, -1),
}


@dataclass
class Entry:
    direction: Direction
    distance: int

    @classmethod
    def from_line(cls, line: str) -> Self:
        _, _, color_part = line.split()
        color = color_part.strip("()#")

        distance_part = color[:-1]
        direction_part = color[-1]

        distance = int(distance_part, base=16)
        direction = Direction(direction_part)

        return cls(direction, distance)


def get_corners(plan: list[Entry]) -> list[Corner]:
    corners = [(0, 0)]

    for entry in plan:
        r, c = corners[-1]
        dr, dc = SHIFTS[entry.direction]
        corners.append((r + dr * entry.distance, c + dc * entry.distance))

    return corners


def get_gauss_area(corners: list[Corner]) -> int:
    a = 0
    b = 0

    for i in range(len(corners) - 1):
        a += corners[i][0] * corners[i + 1][1]
        b += corners[i][1] * corners[i + 1][0]

    return abs(a - b) // 2


def solve(task: str) -> int:
    plan = [Entry.from_line(line) for line in task.splitlines()]
    corners = get_corners(plan)
    return get_gauss_area(corners)
