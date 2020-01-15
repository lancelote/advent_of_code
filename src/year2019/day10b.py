import math
from collections import defaultdict
from typing import Tuple

from src.year2019.day10a import Chart as BaseChart


class Chart(BaseChart):
    def distance_to(self, x: int, y: int) -> float:
        return math.sqrt((x - self.base_x)**2 + (y - self.base_y)**2)

    def remove_till(self, n: int):
        azimuths = defaultdict(list)

        for x, y in self.get_asteroids():
            angle = self.atan2(x, y)
            distance = self.distance_to(x, y)
            azimuths[angle].append((distance, x, y))

        for distances in azimuths.values():
            distances.sort(reverse=True)

        for _, distances in sorted(azimuths.items(), reverse=True):
            n -= 1
            _, x, y = distances.pop()
            if n == 0:
                return x, y

    @property
    def station_location(self) -> Tuple[int, int]:
        station_x = 0
        station_y = 0
        visible_asteroids = 0

        for x, y in self.get_asteroids():
            visible = self.visible_from(x, y)
            if visible > visible_asteroids:
                visible_asteroids = visible
                station_x = x
                station_y = y

        return station_x, station_y


def solve(task: str) -> int:
    chart = Chart.from_string(task)
    station_x, station_y = chart.station_location
    chart.set_base(station_y, station_y)
    x, y = chart.remove_till(200)
    return x * 100 + y
