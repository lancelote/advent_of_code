"""2019 - Day 6 Part 2: Universal Orbit Map."""
from collections import defaultdict
from typing import DefaultDict
from typing import Set

MAP = DefaultDict[str, Set]


def process_data(data: str) -> MAP:
    """Create a orbit map from raw data."""
    orbit_map: MAP = defaultdict(set)

    for line in data.strip().split("\n"):
        obj1, obj2 = line.split(")")
        orbit_map[obj1].add(obj2)
        orbit_map[obj2].add(obj1)

    return orbit_map


def closest_distance(start: str, stop: str, orbit_map: MAP) -> int:
    """Find closest distance between start and stop."""
    distance = 0
    to_visit_now = {start}
    to_visit_next = set()

    while to_visit_now:
        for node in to_visit_now:
            if node == stop:
                return distance - 2
            else:
                to_visit_next.update(orbit_map[node])

        distance += 1
        to_visit_now = to_visit_next - to_visit_now
        to_visit_next = set()

    return -1


def solve(task: str) -> int:
    """Calculate closest distance between YOU and SAN."""
    orbit_map = process_data(task)
    return closest_distance("YOU", "SAN", orbit_map)
