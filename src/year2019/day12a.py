"""2019 - Day 12 Part 1: The N-Body Problem."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple


@dataclass
class Moon:
    x: int
    y: int
    z: int

    @staticmethod
    def from_string(string: str) -> Moon:
        x, y, z = [int(part[2:]) for part in string[1:-1].split(', ')]
        return Moon(x, y, z)


def process_data(data: str) -> Tuple[Moon, Moon, Moon, Moon]:
    moons = data.strip().split('\n')
    # ToDo: finish function

    raise NotImplementedError


def solve(task: str) -> int:
    raise NotImplementedError
