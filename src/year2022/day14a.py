"""2022 - Day 14 Part 1: Regolith Reservoir."""

from __future__ import annotations

import sys
from dataclasses import dataclass
from typing import TypeAlias

Point: TypeAlias = tuple[int, int]
Section: TypeAlias = tuple[Point, Point]


def parse_point(text: str) -> Point:
    """From "519,81" to (519, 81)."""
    x_str, y_str = text.split(",")

    x = int(x_str)
    y = int(y_str)

    return x, y


def parse_sections(task: str) -> list[Section]:
    """From "1,2 -> 2,3 -> 3,4" to [((1, 2), (2, 3)), ((2, 3), (3, 4))]."""
    sections: list[Section] = []

    for line in task.splitlines():
        points = [parse_point(x) for x in line.split(" -> ")]

        for i in range(1, len(points)):
            sections.append((points[i - 1], points[i]))

    return sections


def find_limits(sections: list[Section]) -> tuple[int, int, int, int]:
    min_x, max_x, min_y, max_y = sys.maxsize, 0, sys.maxsize, 0

    for (x1, y1), (x2, y2) in sections:
        min_x = min(min_x, x1, x2)
        max_x = max(max_x, x1, x2)

        min_y = min(min_y, y1, y2)
        max_y = max(max_y, y1, y2)

    min_x = min(min_x, 500)
    max_x = max(max_x, 500)

    min_y = min(min_y, 0)
    max_y = max(max_y, 0)

    return min_x, max_x, min_y, max_y


@dataclass
class Cave:
    data: list[list[bool]]
    grains: int = 0
    is_full: bool = False
    min_x: int = 0
    min_y: int = 0

    @classmethod
    def from_sections(cls, sections: list[Section]) -> Cave:
        min_x, max_x, min_y, max_y = find_limits(sections)

        rows = max_y - min_y + 1
        cols = max_x - min_x + 1

        data = [[False] * cols for _ in range(rows)]

        for (x1, y1), (x2, y2) in sections:
            if x1 == x2:
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    data[y - min_y][x1 - min_x] = True

            elif y1 == y2:
                for x in range(min(x1, x2), max(x1, x2) + 1):
                    data[y1 - min_y][x - min_x] = True

            else:
                raise ValueError("diagonal section detected")

        return cls(data, min_x=min_x, min_y=min_y)

    def drop_grain(self) -> None:
        x, y = 500 - self.min_x, 0 - self.min_y

        try:
            while True:
                if self.is_empty(x, y + 1):
                    x, y = x, y + 1
                elif self.is_empty(x - 1, y + 1):
                    x, y = x - 1, y + 1
                elif self.is_empty(x + 1, y + 1):
                    x, y = x + 1, y + 1
                else:
                    self.data[y][x] = True
                    self.grains += 1
                    break
        except IndexError:
            self.is_full = True

    def is_empty(self, x: int, y: int) -> bool:
        rows = len(self.data)
        cols = len(self.data[0])

        if 0 <= x < cols and 0 <= y < rows:
            return not self.data[y][x]
        else:
            raise IndexError

    def print(self) -> None:
        for row in self.data:
            print("".join("#" if x else "." for x in row))


def solve(task: str) -> int:
    sections = parse_sections(task)
    cave = Cave.from_sections(sections)

    while not cave.is_full:
        cave.drop_grain()

    return cave.grains
