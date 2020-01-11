"""2019 - Day 10 Part 1: Monitoring Station."""

from __future__ import annotations

import math
from dataclasses import dataclass

from typing import List


@dataclass
class Chart:
    """A map of asteroids."""

    locations: List[List[bool]]

    @classmethod
    def from_string(cls, string: str) -> Chart:
        """Covert a raw task into a chart."""
        return cls([
            [location == '#' for location in line]
            for line in string.strip().split('\n')
        ])

    def unique_inclinations_from(self, base_x: int, base_y: int) -> int:
        """Find the number of visible asteroids from this one."""
        inclinations = set()

        for y in range(len(self.locations)):
            for x in range(len(self.locations[0])):
                if self.locations[y][x] and not (x == base_x and y == base_y):
                    new_x = x - base_x
                    new_y = y - base_y
                    tan = new_y / new_x if new_x else math.inf
                    inclinations.add((new_x > 0, new_y > 0, tan))

        return len(inclinations)

    @property
    def most_observant(self) -> int:
        """Return most observable asteroid."""
        return max(
            self.unique_inclinations_from(x, y)
            for x in range(len(self.locations[0]))
            for y in range(len(self.locations))
            if self.locations[y][x]
        )


def solve(task: str) -> int:
    """Find most observable asteroid."""
    chart = Chart.from_string(task)
    return chart.most_observant
