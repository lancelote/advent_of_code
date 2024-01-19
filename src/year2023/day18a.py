"""2023 - Day 18 Part 1: Lavaduct Lagoon"""
import sys
from dataclasses import dataclass
from enum import Enum
from typing import Self


class Direction(Enum):
    U = "U"
    R = "R"
    D = "D"
    L = "L"


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
    color: str

    @classmethod
    def from_line(cls, line: str) -> Self:
        dir_part, dist_part, color_part = line.split()

        direction = Direction(dir_part)
        distance = int(dist_part)
        color = color_part.strip("()")

        return cls(direction, distance, color)


def dig_trench(plan: list[Entry]) -> set[tuple[int, int]]:
    points: set[tuple[int, int]] = set()

    r, c = 0, 0

    for entry in plan:
        dr, dc = SHIFTS[entry.direction]

        for _ in range(entry.distance):
            r += dr
            c += dc

            points.add((r, c))

    return points


def print_trench(trench: set[tuple[int, int]]) -> None:
    min_r, max_r = sys.maxsize, 0
    min_c, max_c = sys.maxsize, 0

    for r, c in trench:
        min_r = min(min_r, r)
        max_r = max(max_r, r)

        min_c = min(min_c, c)
        max_c = max(max_c, c)

    rows = max_r - min_r + 1
    cols = max_c - min_c + 1

    ground = [["."] * cols for _ in range(rows)]

    for r, c in trench:
        ground[r - min_r][c - min_c] = "#"

    print("\n".join("".join(line) for line in ground))


def solve(task: str) -> int:
    plan = [Entry.from_line(line) for line in task.splitlines()]
    trench = dig_trench(plan)
    print_trench(trench)
