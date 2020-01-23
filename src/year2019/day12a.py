"""2019 - Day 12 Part 1: The N-Body Problem."""

from __future__ import annotations

from dataclasses import dataclass
from typing import List


@dataclass
class Moon:
    x: int
    y: int
    z: int

    dx: int = 0
    dy: int = 0
    dz: int = 0

    def apply_velocity(self):
        self.x += self.dx
        self.y += self.dy
        self.z += self.dz

    @classmethod
    def from_string(cls, string: str) -> Moon:
        x, y, z = [int(part[2:]) for part in string[1:-1].split(', ')]
        return cls(x, y, z)


@dataclass
class System:
    moons: List[Moon]

    @classmethod
    def from_raw_data(cls, data: str) -> System:
        moons = [Moon.from_string(line) for line in data.strip().split('\n')]
        return cls(moons)


def solve(task: str) -> int:
    raise NotImplementedError
