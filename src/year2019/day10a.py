"""2019 - Day 10 Part 1: Monitoring Station."""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Dict, Generator, List, Tuple


@dataclass
class Chart:
    """A map of asteroids."""

    locations: List[List[bool]]
    base_x: int = 0
    base_y: int = 0

    @classmethod
    def from_string(cls, string: str) -> Chart:
        """Covert a raw task into a chart."""
        return cls(
            [
                [location == "#" for location in line]
                for line in string.strip().split("\n")
            ]
        )

    def not_base(self, x: int, y: int) -> bool:
        """Check if a given point is a base."""
        return not (x == self.base_x and y == self.base_y)

    def set_base(self, x: int, y: int):
        """Update base."""
        self.base_x = x
        self.base_y = y

    def asteroids(self) -> Generator[Tuple[int, int], None, None]:
        """Iterate over all iterate excluding base."""
        for y in range(len(self.locations)):
            for x in range(len(self.locations[0])):
                if self.locations[y][x] and self.not_base(x, y):
                    yield x, y

    def atan2(self, x: int, y: int) -> float:
        """Compute arctangent to a given point."""
        norm_x = x - self.base_x
        norm_y = self.base_y - y

        incl_x = -norm_y
        incl_y = norm_x

        return math.atan2(incl_y, incl_x)

    def distance_to(self, x: int, y: int) -> float:
        """Return distance to a given coordinates."""
        norm_x = x - self.base_x
        norm_y = self.base_y - y

        incl_x = -norm_y
        incl_y = norm_x

        return math.sqrt(incl_x ** 2 + incl_y ** 2)

    def seen_from(self, base_x: int, base_y: int) -> int:
        """Find the number of visible asteroids from this one."""
        self.set_base(base_x, base_y)
        return len({self.atan2(x, y) for x, y in self.asteroids()})

    def remove_till(self, n: int) -> Tuple[int, int]:
        """Remove n asteroids and return coordinates of the next one."""
        azimuths: Dict[float, List[Tuple[float, int, int]]] = dict()

        for x, y in self.asteroids():
            angle = self.atan2(x, y)
            distance = self.distance_to(x, y)
            if angle in azimuths:
                azimuths[angle].append((distance, x, y))
            else:
                azimuths[angle] = [(distance, x, y)]

        for distances in azimuths.values():
            distances.sort(reverse=True)

        sorted_angles = sorted(azimuths.keys(), reverse=True)
        empty_angles: List[float] = []

        while len(empty_angles) != len(sorted_angles):
            for angle in sorted_angles:
                if angle in empty_angles:
                    continue
                if not azimuths[angle]:
                    empty_angles.append(angle)
                    continue
                n -= 1
                _, x, y = azimuths[angle].pop()
                if n == 0:
                    return x, y

        raise ValueError(f"cannot reach {n} asteroid")

    @property
    def optimal_station_position(self) -> Tuple[int, int, int]:
        """Return optimal coordinates and the number of visible asteroids."""
        return max((self.seen_from(x, y), x, y) for x, y in self.asteroids())

    @property
    def most_observant(self) -> int:
        """Return most observable asteroid."""
        return self.optimal_station_position[0]


def solve(task: str) -> int:
    """Find most observable asteroid."""
    chart = Chart.from_string(task)
    return chart.most_observant
