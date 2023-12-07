"""2023 - Day 6 Part 1: Wait For It"""
import math
from dataclasses import dataclass


@dataclass
class Race:
    time: int
    dist: int

    @property
    def ways_to_win(self) -> int:
        # behold The Math

        low = (self.time - math.sqrt(self.time**2 - 4 * self.dist)) / 2
        high = (self.time + math.sqrt(self.time**2 - 4 * self.dist)) / 2

        low += 1e-9
        high -= 1e-9

        return math.floor(high) - math.ceil(low) + 1


def process_data(data: str) -> list[Race]:
    lines = data.splitlines()
    time_parts = lines[0].split()
    dist_parts = lines[1].split()

    times = [int(time_parts[i]) for i in range(1, len(time_parts))]
    dists = [int(dist_parts[i]) for i in range(1, len(dist_parts))]

    return [Race(t, d) for t, d in zip(times, dists)]


def solve(task: str) -> int:
    result = 1
    races = process_data(task)

    for race in races:
        result *= race.ways_to_win

    return result
