"""2019 - Day 12 Part 1: The N-Body Problem."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple


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

    @staticmethod
    def from_string(string: str) -> Moon:
        x, y, z = [int(part[2:]) for part in string[1:-1].split(', ')]
        return Moon(x, y, z)


def process_data(data: str) -> Tuple[Moon, Moon, Moon, Moon]:
    moons = [Moon.from_string(line) for line in data.strip().split('\n')]
    io, europa, ganymede, callisto = moons
    return io, europa, ganymede, callisto


def solve(task: str) -> int:
    raise NotImplementedError
