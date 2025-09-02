"""2018 - Day 6 Part 1: Chronal Coordinates."""

from __future__ import annotations

import math
from collections import defaultdict
from operator import itemgetter
from string import ascii_lowercase
from typing import Any, DefaultDict, TypeVar

T = TypeVar("T", bound="Grid")


class Coordinate:
    """Abstract cartesian coordinate."""

    def __init__(self, x: int, y: int):
        """Where x and y are cartesian coordinates."""
        self.x = x
        self.y = y

    def __sub__(self, other: Coordinate) -> int:
        return abs(self.x - other.x) + abs(self.y - other.y)

    def __eq__(self, other: Any) -> bool:
        assert isinstance(other, Coordinate)
        return self.x == other.x and self.y == other.y

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def __str__(self) -> str:
        """E.g. `Coordinate(x, y)`."""
        return f"{self.__class__.__name__}({self.x}, {self.y})"


class Dot(Coordinate):
    """A dot of the grid."""

    def __init__(self, x: int, y: int):
        """With the closest pin reference and distance to it."""
        self.closest: Pin | None = None
        self.distance: int | float = math.inf
        super().__init__(x, y)


class Pin(Coordinate):
    """A pin coordinate in time."""

    @classmethod
    def from_string(cls, line: str) -> Pin:
        """From '81, 252' string."""
        x, y = line.split(", ")
        return cls(int(x), int(y))

    @classmethod
    def parse_task(cls, task: str) -> list[Pin]:
        """Parse one coordinate per line from task input."""
        return [Pin.from_string(line) for line in task.strip().split("\n")]


class Grid:
    """A gird of time dots with pins."""

    def __init__(
        self, pins: list[Pin], dots: list[Dot], width: int, height: int
    ):
        """With list pof pins and dots on the grid."""
        self.pins = pins
        self.dots = dots
        self.width = width
        self.height = height

    def __eq__(self, other: Any) -> bool:
        assert isinstance(other, Grid)
        return all(
            [
                self.pins == other.pins,
                self.dots == other.dots,
                self.width == other.width,
                self.height == other.height,
            ]
        )

    @classmethod
    def parse_task(cls: type[T], task: str) -> T:
        """Parse one coordinate per line from task input."""
        dots: list[Dot] = []
        pins: list[Pin] = Pin.parse_task(task)

        width = max(pins, key=lambda pin: pin.x).x + 1
        height = max(pins, key=lambda pin: pin.y).y + 1

        for x in range(width):
            for y in range(height):
                dots.append(Dot(x, y))

        return cls(pins, dots, width, height)

    def calc_distances(self) -> None:
        """Calculate the closest pin for each dot of the grid."""
        for pin in self.pins:
            for dot in self.dots:
                distance = pin - dot
                if dot.distance > distance:
                    dot.distance = distance
                    dot.closest = pin
                elif dot.distance == distance:
                    dot.closest = None

    @property
    def largest_area(self) -> int:
        """Find the biggest pin area."""
        banned_x = {0, self.width}
        banned_y = {0, self.height}
        infinite: set[Pin] = set()
        areas: DefaultDict[Pin, int] = defaultdict(int)

        self.calc_distances()

        for dot in self.dots:
            if dot.closest is None:
                continue
            if dot.x in banned_x or dot.y in banned_y:
                infinite.add(dot.closest)
            elif dot.closest not in infinite:
                areas[dot.closest] += 1

        _, largest_area = max(areas.items(), key=itemgetter(1))
        return largest_area

    def display(self) -> None:
        """Print grid in a human-readable view."""
        names = {}
        for pin, name in zip(self.pins, ascii_lowercase):
            names[pin] = name

        data = [["." for _ in range(self.width)] for _ in range(self.height)]
        for dot in self.dots:
            if dot.closest is None:
                data[dot.y][dot.x] = "."
            else:
                data[dot.y][dot.x] = names.get(dot.closest, ".")

        print("\n".join("".join(row) for row in data))


def solve(task: str) -> int:
    """Find the biggest pin area of the grid."""
    grid = Grid.parse_task(task)
    return grid.largest_area
