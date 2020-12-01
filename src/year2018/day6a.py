"""2018 - Day 6 Part 1: Chronal Coordinates.

The device on your wrist beeps several times, and once again you feel like
you're falling.

"Situation critical," the device announces. "Destination indeterminate. Chronal
interference detected. Please specify new target coordinates."

The device then produces a list of coordinates (your puzzle input). Are they
places it thinks are safe or dangerous? It recommends you check manual page
729. The Elves did not give you a manual.

If they're dangerous, maybe you can minimize the danger by finding the
coordinate that gives the largest distance from the other points.

Using only the Manhattan distance, determine the area around each coordinate by
counting the number of integer X,Y locations that are closest to that
coordinate (and aren't tied in distance to any other coordinate).

Your goal is to find the size of the largest area that isn't infinite. For
example, consider the following list of coordinates:

    1, 1
    1, 6
    8, 3
    3, 4
    5, 5
    8, 9

If we name these coordinates A through F, we can draw them on a grid, putting
0,0 at the top left:

    ..........
    .A........
    ..........
    ........C.
    ...D......
    .....E....
    .B........
    ..........
    ..........
    ........F.

This view is partial - the actual grid extends infinitely in all directions.
Using the Manhattan distance, each location's closest coordinate can be
determined, shown here in lowercase:

    aaaaa.cccc
    aAaaa.cccc
    aaaddecccc
    aadddeccCc
    ..dDdeeccc
    bb.deEeecc
    bBb.eeee..
    bbb.eeefff
    bbb.eeffff
    bbb.ffffFf

Locations shown as . are equally far from two or more coordinates, and so they
don't count as being closest to any.

In this example, the areas of coordinates A, B, C, and F are infinite - while
not shown here, their areas extend forever outside the visible grid. However,
the areas of coordinates D and E are finite: D is closest to 9 locations, and
E is closest to 17 (both including the coordinate's location itself).
Therefore, in this example, the size of the largest area is 17.

What is the size of the largest area that isn't infinite?
"""

from __future__ import annotations

import math
from abc import ABC
from collections import defaultdict
from operator import itemgetter
from string import ascii_lowercase
from typing import Any, DefaultDict, List, Optional, Set, Union


class Coordinate(ABC):
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

    def __hash__(self):
        return hash((self.x, self.y))

    def __str__(self) -> str:
        """E.g. `Coordinate(x, y)`."""
        return f"{self.__class__.__name__}({self.x}, {self.y})"


class Dot(Coordinate):
    """A dot of the grid."""

    def __init__(self, x: int, y: int):
        """With closest pin reference and distance to it."""
        self.closest: Optional[Pin] = None
        self.distance: Union[int, float] = math.inf
        super().__init__(x, y)


class Pin(Coordinate):
    """A pin coordinate in time."""

    @classmethod
    def from_string(cls, line: str) -> Pin:
        """From '81, 252' string."""
        x, y = line.split(", ")
        return cls(int(x), int(y))

    @classmethod
    def parse_task(cls, task: str) -> List[Pin]:
        """Parse one coordinate per line from task input."""
        return [Pin.from_string(line) for line in task.strip().split("\n")]


class Grid:
    """A gird of time dots with pins."""

    def __init__(
        self, pins: List[Pin], dots: List[Dot], width: int, height: int
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
    def parse_task(cls, task: str):
        """Parse one coordinate per line from task input."""
        dots: List[Dot] = []
        pins: List[Pin] = Pin.parse_task(task)

        width = max(pins, key=lambda pin: pin.x).x + 1
        height = max(pins, key=lambda pin: pin.y).y + 1

        for x in range(width):
            for y in range(height):
                dots.append(Dot(x, y))

        return cls(pins, dots, width, height)

    def calc_distances(self):
        """Calculate closest pin for each dot of the grid."""
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
        infinite: Set[Pin] = set()
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

    def display(self):
        """Print grid in a human readable view."""
        names = {}
        for pin, name in zip(self.pins, ascii_lowercase):
            names[pin] = name

        data = [["." for _ in range(self.width)] for _ in range(self.height)]
        for dot in self.dots:
            data[dot.y][dot.x] = names.get(dot.closest, ".")

        print("\n".join("".join(row) for row in data))


def solve(task: str) -> int:
    """Find the biggest pin area of the grid."""
    grid = Grid.parse_task(task)
    return grid.largest_area
