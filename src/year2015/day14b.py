"""2015 - Day 14 Part 2: Reindeer Olympics."""

from src.year2015.day14a import Reindeer
from src.year2015.day14a import process_data


def max_points_after(deers: list[Reindeer], seconds: int) -> int:
    distances = [0] * len(deers)
    points = [0] * len(deers)

    for second in range(1, seconds + 1):
        max_distance = 0

        for i, deer in enumerate(deers):
            distances[i] = deer.distance_after(second)
            max_distance = max(max_distance, distances[i])

        for i, distance in enumerate(distances):
            if distance == max_distance:
                points[i] += 1

    return max(points)


def solve(task: str) -> int:
    deers = process_data(task)
    return max_points_after(deers, 2503)
