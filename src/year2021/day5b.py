from __future__ import annotations

from collections import defaultdict
from typing import Iterator


def iter_ints(a: int, b: int) -> Iterator[int]:
    if a < b:
        for x in range(a, b + 1):
            yield x
    elif a > b:
        for x in range(a, b - 1, -1):
            yield x
    else:
        raise ValueError("iterating between equal ints")


class Floor:
    def __init__(self) -> None:
        self.points: dict[Point, int] = defaultdict(int)

    def draw(self, segments: list[Segment]) -> None:
        for segment in segments:
            for point in segment.iter_points():
                self.points[point] += 1

    @property
    def num_overlap(self) -> int:
        return sum(1 for k, v in self.points.items() if v >= 2)


class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    @classmethod
    def from_str(cls, line: str) -> Point:
        x_s, y_s = line.split(",")
        return cls(int(x_s), int(y_s))

    def __str__(self) -> str:
        return f"Point(x={self.x}, y={self.y})"

    __repr__ = __str__

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Point):
            raise ValueError(f"comparing point with {type(other)}")
        return self.x == other.x and self.y == other.y

    def __hash__(self) -> int:
        return (self.x, self.y).__hash__()


class Segment:
    def __init__(self, start: Point, stop: Point) -> None:
        self.start = start
        self.end = stop

    @classmethod
    def from_line(cls, line: str) -> Segment:
        start_s, stop_s = line.split(" -> ")
        return cls(Point.from_str(start_s), Point.from_str(stop_s))

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
        if self.is_horizontal:
            for x in iter_ints(self.start.x, self.end.x):
                yield Point(x, self.start.y)
        elif self.is_vertical:
            for y in iter_ints(self.start.y, self.end.y):
                yield Point(self.start.x, y)
        else:
            iter_x = iter_ints(self.start.x, self.end.x)
            iter_y = iter_ints(self.start.y, self.end.y)
            for x, y in zip(iter_x, iter_y):
                yield Point(x, y)

    def __str__(self) -> str:
        return f"Segment(start={self.start}, end={self.end})"

    __repr__ = __str__


def solve(task: str) -> int:
    segments = [Segment.from_line(line) for line in task.splitlines()]

    floor = Floor()
    floor.draw(segments)

    return floor.num_overlap
