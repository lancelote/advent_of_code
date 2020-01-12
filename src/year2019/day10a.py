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

    def visible_from(self, base_x: int, base_y: int) -> int:
        """Find the number of visible asteroids from this one."""
        azimuth = set()

        for y in range(len(self.locations)):
            for x in range(len(self.locations[0])):
                if self.locations[y][x] and not (x == base_x and y == base_y):
                    azimuth.add(math.atan2(y - base_y, x - base_x))

        return len(azimuth)

    @property
    def most_observant(self) -> int:
        """Return most observable asteroid."""
        return max(
            self.visible_from(x, y)
            for x in range(len(self.locations[0]))
            for y in range(len(self.locations))
            if self.locations[y][x]
        )


def solve(task: str) -> int:
    """Find most observable asteroid."""
    chart = Chart.from_string(task)
    return chart.most_observant
