"""2019 - Day 11 Part 1: Space Police tests."""

from collections import deque
from dataclasses import dataclass, field
from typing import Deque

from src.year2019.day11a import (
    Robot,
    Direction,
    Coordinates,
    Hull,
    Color,
    Panel,
    Computer,
)


@dataclass
class MockComputer(Computer):
    stdin: Deque[int] = field(default_factory=deque)
    stdout: Deque[int] = field(default_factory=deque)

    def execute(self):
        pass


def test_robot_example_walk_through():
    hull = Hull(Panel)
    cpu = MockComputer()
    robot = Robot(cpu)

    assert robot.direction is Direction.UP
    assert robot.coordinates == Coordinates(0, 0)

    cpu.stdout.append(1)  # paint white
    cpu.stdout.append(0)  # turn left

    robot.step(hull)
    assert robot.direction is Direction.LEFT
    assert robot.coordinates == Coordinates(-1, 0)
    assert hull[Coordinates(0, 0)].color is Color.WHITE
