from __future__ import annotations

from collections import defaultdict
from itertools import repeat
from typing import Iterable
from typing import Iterator
from typing import NamedTuple


def range_between(a: int, b: int) -> Iterable[int]:
    """Get a range from a to b inclusively (can do reverse)."""
    if a < b:
        return range(a, b + 1, 1)
    else:
        return range(a, b - 1, -1)


class Floor:
    """Ocean floor."""

    def __init__(self) -> None:
        self.overlaps: dict[Point, int] = defaultdict(int)

    def draw(self, segments: list[Segment]) -> None:
        for segment in segments:
            for point in segment.iter_points():
                self.overlaps[point] += 1

    @property
    def num_overlap(self) -> int:
        return sum(1 for _, overlap in self.overlaps.items() if overlap >= 2)


class Point(NamedTuple):
    x: int
    y: int

    @classmethod
    def from_str(cls, line: str) -> Point:
        x_s, y_s = line.split(",")
        return cls(int(x_s), int(y_s))


class Segment:
    def __init__(self, start: Point, stop: Point) -> None:
        self.start = start
        self.end = stop

    @classmethod
    def from_line(cls, line: str) -> Segment:
        start_s, end_s = line.split(" -> ")
        start = Point.from_str(start_s)
        end = Point.from_str(end_s)
        return cls(start, end)

    @property
    def is_horizontal(self) -> bool:
        return self.start.y == self.end.y

    @property
    def is_vertical(self) -> bool:
        return self.start.x == self.end.x

    @property
    def is_diagonal(self) -> bool:
        return not (self.is_vertical or self.is_horizontal)

    def iter_points(self) -> Iterator[Point]:
        iter_x = range_between(self.start.x, self.end.x)
        iter_y = range_between(self.start.y, self.end.y)

        if self.is_horizontal:
            iter_y = repeat(self.start.y)
        elif self.is_vertical:
            iter_x = repeat(self.start.x)

        for x, y in zip(iter_x, iter_y):
            yield Point(x, y)

    def __str__(self) -> str:
        return f"Segment(start={self.start}, end={self.end})"

    __repr__ = __str__


def solve(task: str) -> int:
    segments = [Segment.from_line(line) for line in task.splitlines()]
    segments = [segment for segment in segments if not segment.is_diagonal]

    floor = Floor()
    floor.draw(segments)

    return floor.num_overlap
