"""2022 - Day 14 Part 2: Regolith Reservoir."""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from src.year2022.day14a import parse_sections
from src.year2022.day14a import Point
from src.year2022.day14a import Section


class Material(Enum):
    ROCK = "#"
    SAND = "o"


def find_floor(sections: list[Section]) -> int:
    max_y = 0

    for (_, y1), (_, y2) in sections:
        max_y = max(max_y, y1, y2)

    return 2 + max_y


@dataclass
class Cave:
    data: dict[Point, Material]
    floor: int
    is_full: bool = False

    @classmethod
    def from_sections(cls, sections: list[Section]) -> Cave:
        floor = find_floor(sections)
        data: dict[Point, Material] = {}

        for (x1, y1), (x2, y2) in sections:
            if x1 == x2:
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    data[(x1, y)] = Material.ROCK

            elif y1 == y2:
                for x in range(min(x1, x2), max(x1, x2) + 1):
                    data[(x, y1)] = Material.ROCK

            else:
                raise ValueError("diagonal section detected")

        return cls(data, floor)

    def is_empty(self, x: int, y: int) -> bool:
        return y != self.floor and (x, y) not in self.data

    def drop_grain(self) -> None:
        x, y = 500, 0

        while True:
            if self.is_empty(x, y + 1):
                x, y = x, y + 1
            elif self.is_empty(x - 1, y + 1):
                x, y = x - 1, y + 1
            elif self.is_empty(x + 1, y + 1):
                x, y = x + 1, y + 1
            elif not self.is_empty(x, y):
                self.is_full = True
                break
            else:
                self.data[(x, y)] = Material.SAND
                break

    @property
    def grains(self) -> int:
        return sum(x is Material.SAND for x in self.data.values())


def solve(task: str) -> int:
    sections = parse_sections(task)
    cave = Cave.from_sections(sections)

    while not cave.is_full:
        cave.drop_grain()

    return cave.grains
