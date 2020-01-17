import math
from collections import defaultdict
from typing import Tuple

from src.year2019.day10a import Chart as BaseChart


class Chart(BaseChart):
    def distance_to(self, x: int, y: int) -> float:
        return math.sqrt((x - self.base_x)**2 + (y - self.base_y)**2)

    def remove_till(self, n: int) -> Tuple[int, int]:
        azimuths = defaultdict(list)

        for x, y in self.asteroids():
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


def solve(task: str) -> int:
    chart = Chart.from_string(task)
    _, station_x, station_y = chart.optimal_station_position
    chart.set_base(station_y, station_y)
    x, y = chart.remove_till(200)
    return x * 100 + y
