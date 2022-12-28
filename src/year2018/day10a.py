"""2018 - Day 10 Part 1: The Stars Align."""
from __future__ import annotations

import re
from dataclasses import dataclass


@dataclass
class Point:
    """Rescue point on the sky."""

    x: int
    y: int
    dx: int
    dy: int

    @classmethod
    def from_line(cls, line: str) -> Point:
        """Get Point from the line."""
        return cls(*map(int, re.findall(r"[\d-]+", line)))

    @classmethod
    def parse_task(cls, task: str) -> list[Point]:
        """Parse the given task returning a list of rescue points."""
        return [cls.from_line(line) for line in task.strip().split("\n")]

    def move(self) -> None:
        """Move a star by one tick."""
        self.x += self.dx
        self.y += self.dy

    def back(self) -> None:
        """Go back in time by one tick."""
        self.x -= self.dx
        self.y -= self.dy


@dataclass
class Sky:
    """Sky with given rescue points."""

    points: list[Point]

    def move(self) -> None:
        """Move sky by one tick forward in time."""
        for point in self.points:
            point.move()

    def back(self) -> None:
        """Move sky by one tick backwards in time."""
        for point in self.points:
            point.back()

    def bounds(self) -> tuple[int, int, int, int]:
        """Get extremum points."""
        min_x = min(point.x for point in self.points)
        max_x = max(point.x for point in self.points)
        min_y = min(point.y for point in self.points)
        max_y = max(point.y for point in self.points)
        return min_x, max_x, min_y, max_y

    def move_till_min_area(self) -> int:
        """Move in time till rescue points have a minimum area in the sky."""
        seconds = 0
        current_area = self.area
        self.move()

        while self.area < current_area:
            current_area = self.area
            self.move()
            seconds += 1

        self.back()
        return seconds

    @property
    def area(self) -> int:
        """Calculate the rescue point area in the sky."""
        min_x, max_x, min_y, max_y = self.bounds()
        return (max_x - min_x + 1) * (max_y - min_y + 1)

    def __str__(self) -> str:
        min_x, max_x, min_y, max_y = self.bounds()

        sky = []
        for _ in range(min_y, max_y + 1):
            line = []
            for _ in range(min_x, max_x + 1):
                line.append(".")
            sky.append(line)

        for point in self.points:
            sky[point.y - min_y][point.x - min_x] = "#"

        return "\n".join("".join(line) for line in sky)


def solve(task: str) -> None:
    """Find a message in the sky."""
    points = Point.parse_task(task)
    sky = Sky(points)
    sky.move_till_min_area()
    print(sky)
