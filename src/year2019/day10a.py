"""2019 - Day 10 Part 1: Monitoring Station."""

from __future__ import annotations

import math
from dataclasses import dataclass

from typing import List, Tuple


@dataclass
class Chart:
    """A map of asteroids."""

    locations: List[List[bool]]
    base_x: int = 0
    base_y: int = 0

    @classmethod
    def from_string(cls, string: str) -> Chart:
        """Covert a raw task into a chart."""
        return cls([
            [location == '#' for location in line]
            for line in string.strip().split('\n')
        ])

    def not_base(self, x: int, y: int) -> bool:
        """Check if a given point is a base."""
        return not (x == self.base_x and y == self.base_y)

    def set_base(self, x: int, y: int):
        """Update base."""
        self.base_x = x
        self.base_y = y

    def get_asteroids(self) -> Tuple[int, int]:
        """Iterate over all iterate excluding base."""
        for y in range(len(self.locations)):
            for x in range(len(self.locations[0])):
                if self.locations[y][x] and self.not_base(x, y):
                    yield x, y

    def atan2(self, x: int, y: int) -> float:
        """Compute arctangent to a given point."""
        return math.atan2(y - self.base_y, x - self.base_x)

    def visible_from(self, base_x: int, base_y: int) -> int:
        """Find the number of visible asteroids from this one."""
        self.set_base(base_x, base_y)
        return len({self.atan2(x, y) for x, y in self.get_asteroids()})

    @property
    def most_observant(self) -> int:
        """Return most observable asteroid."""
        return max(self.visible_from(x, y) for x, y in self.get_asteroids())


def solve(task: str) -> int:
    """Find most observable asteroid."""
    chart = Chart.from_string(task)
    return chart.most_observant
