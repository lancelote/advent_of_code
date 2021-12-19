"""2021 - Day 17 Part 1: Trick Shot."""
from __future__ import annotations

import re
from dataclasses import dataclass


@dataclass(frozen=True)
class Velocity:
    dx: int
    dy: int


@dataclass(frozen=True)
class Target:
    left_x: int
    right_x: int
    bottom_y: int
    top_y: int

    @classmethod
    def from_line(cls, line: str) -> Target:
        return cls(*[int(x) for x in re.findall(r"-?\d+", line)])


class Trajectory:
    def __init__(self, velocity: Velocity, target: Target) -> None:
        self.max_y = 0

        self.x = 0
        self.y = 0

        self.dx = velocity.dx
        self.dy = velocity.dy

        self.hit = False
        self.too_close = False
        self.too_high = False

        self.target = target

    def calculate(self) -> None:
        while not (self.hit or self.too_close or self.too_high):
            self.step()

    def step(self) -> None:
        self.x += self.dx
        self.check_position()

        self.y += self.dy
        self.max_y = max(self.max_y, self.y)
        self.check_position()

        self.inc_dx()
        self.inc_dy()

    def check_position(self) -> None:
        hit_x = self.target.left_x <= self.x <= self.target.right_x
        hit_y = self.target.bottom_y <= self.y <= self.target.top_y

        if hit_x and hit_y:
            self.hit = True
        elif self.dx == 0 and self.y < self.target.bottom_y:
            self.too_close = True
        elif self.dx >= self.target.left_x and self.y < self.target.bottom_y:
            self.too_high = True

    def inc_dx(self) -> None:
        self.dx = max(0, self.dx - 1)

    def inc_dy(self) -> None:
        self.dy -= 1


def find_max_y(target: Target) -> int:
    dx = 1
    dy = 1
    max_y = 0

    while True:
        velocity = Velocity(dx, dy)
        trajectory = Trajectory(velocity, target)
        trajectory.calculate()

        if trajectory.too_close:
            dx += 1
        elif trajectory.too_high:
            break
        else:
            max_y = trajectory.max_y
            dy += 1

    return max_y


def solve(task: str) -> int:
    target = Target.from_line(task)
    return find_max_y(target)
