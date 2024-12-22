"""2024 - Day 14 Part 2: Restroom Redoubt"""

import sys
from dataclasses import dataclass
from itertools import combinations

from src.year2024.day14a import Robot


def distance(r1: Robot, r2: Robot) -> int:
    return abs(r1.x - r2.x) + abs(r1.y - r2.y)


@dataclass
class Field:
    width: int
    height: int
    robots: list[Robot]

    def make_step(self) -> None:
        for robot in self.robots:
            robot.x = (robot.x + robot.dx) % self.width
            robot.y = (robot.y + robot.dy) % self.height

    @property
    def entropy(self) -> int:
        return sum(distance(a, b) for a, b in combinations(self.robots, 2))

    def __str__(self) -> str:
        data = [[" " for _ in range(self.width)] for _ in range(self.height)]
        for robot in self.robots:
            data[robot.y][robot.x] = "#"
        return "\n".join("".join(line) for line in data)


def solve(task: str, width: int = 101, height: int = 103) -> int:
    robots = [Robot.from_line(x) for x in task.split("\n")]
    field = Field(width, height, robots)

    min_entropy_second = 0
    min_entropy_seen = sys.maxsize

    for i in range(1, 10_000):
        field.make_step()
        field_entropy = field.entropy

        if field_entropy < min_entropy_seen:
            min_entropy_seen = field_entropy
            min_entropy_second = i

    return min_entropy_second
