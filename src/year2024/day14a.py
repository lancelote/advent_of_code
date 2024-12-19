"""2024 - Day 14 Part 1: Restroom Redoubt"""

import re
from collections import Counter
from dataclasses import dataclass
from typing import Self


@dataclass
class Robot:
    x: int
    y: int

    dx: int
    dy: int

    @classmethod
    def from_line(cls, line: str) -> Self:
        a, b, c, d = re.findall(r"[\d\-]+", line)
        return cls(int(a), int(b), int(c), int(d))


@dataclass
class Field:
    width: int
    height: int

    def position_of(self, robot: Robot, after: int) -> tuple[int, int]:
        x = (robot.x + robot.dx * after) % self.width
        y = (robot.y + robot.dy * after) % self.height

        return x, y

    def quadrant_of(self, robot: Robot, after: int) -> int:
        x, y = self.position_of(robot, after)

        middle_x = self.width // 2
        middle_y = self.height // 2

        if x == self.width // 2 or y == self.height // 2:
            return 0
        elif x < middle_x and y < middle_y:
            return 1  # top left
        elif x > middle_x and y < middle_y:
            return 2  # top right
        elif x > middle_x and y > middle_y:
            return 3  # bottom right
        else:
            return 4  # bottom left

    def safety_factor_for(self, robots: list[Robot], after: int) -> int:
        qs = Counter(self.quadrant_of(robot, after) for robot in robots)
        return qs[1] * qs[2] * qs[3] * qs[4]


def solve(task: str, width: int = 101, height: int = 103) -> int:
    robots = [Robot.from_line(x) for x in task.split("\n")]
    field = Field(width, height)
    return field.safety_factor_for(robots, after=100)
