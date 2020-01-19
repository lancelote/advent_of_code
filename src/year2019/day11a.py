from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from enum import Enum

from typing import DefaultDict, NamedTuple

from src.year2019.intcode import Computer


class Direction(Enum):
    UP = '^'
    RIGHT = '>'
    DOWN = 'v'
    LEFT = '<'


LEFT_TURN = {
    Direction.UP: Direction.LEFT,
    Direction.RIGHT: Direction.UP,
    Direction.DOWN: Direction.RIGHT,
    Direction.LEFT: Direction.DOWN
}

RIGHT_TURN = {
    Direction.UP: Direction.RIGHT,
    Direction.RIGHT: Direction.DOWN,
    Direction.DOWN: Direction.LEFT,
    Direction.LEFT: Direction.UP,
}


class Coordinates(NamedTuple):
    x: int = 0
    y: int = 0

    def __add__(self, other: Coordinates) -> Coordinates:
        return Coordinates(self.x + other.x, self.y + other.y)


SHIFT = {
    Direction.UP: Coordinates(0, +1),
    Direction.RIGHT: Coordinates(+1, 0),
    Direction.DOWN: Coordinates(0, -1),
    Direction.LEFT: Coordinates(-1, 0),
}


class Color(Enum):
    WHITE = '#'
    BLACK = '.'


@dataclass
class Panel:
    visited: bool = False
    color: Color = Color.BLACK

    def paint(self, color: Color):
        self.color = color


class Hull:
    def __init__(self):
        self._panels: DefaultDict[Coordinates, Panel] = defaultdict(Panel)

    def __getitem__(self, coordinates: Coordinates) -> Panel:
        panel = self._panels[coordinates]
        panel.visited = True
        return panel

    def values(self):
        return self._panels.values()


class Robot:
    def __init__(self, cpu: Computer = None):
        self.coordinates = Coordinates()
        self.cpu = cpu or Computer()
        self.direction = Direction.UP

    def load_program(self, program: str):
        self.cpu.load_program(program)

    def paint(self, hull: Hull):
        assert self.cpu.program_is_loaded

        while not self.is_halt:
            self.step(hull)

    def step(self, hull: Hull):
        panel = hull[self.coordinates]
        self.cpu.stdin.append(0 if panel.color is Color.BLACK else 1)
        self.cpu.execute()

        angle = self.cpu.stdout.pop()
        new_color = Color.WHITE if self.cpu.stdout.pop() == 1 else Color.BLACK

        panel.paint(new_color)
        self.rotate(angle)
        self.move()

    def rotate(self, angle: int):
        if angle == 0:  # Left
            self.direction = LEFT_TURN[self.direction]
        elif angle == 1:  # Right
            self.direction = RIGHT_TURN[self.direction]
        else:
            raise ValueError(f'unknown angle {angle}')

    def move(self):
        self.coordinates += SHIFT[self.direction]

    @property
    def is_halt(self):
        return self.cpu.is_halt


def solve(task: str) -> int:
    hull = Hull()
    robot = Robot()
    robot.load_program(task)
    robot.paint(hull)
    return len([panel for panel in hull.values() if panel.visited])
