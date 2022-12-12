"""2019 - Day 6 Part 1: Universal Orbit Map."""
from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field


@dataclass
class Object:
    """Celestial object."""

    name: str
    satellites: list[Object] = field(default_factory=list)

    def traverse(self, value: int = 0) -> int:
        """Count direct and indirect orbits for all satellites recursive."""
        return value + sum(obj.traverse(value + 1) for obj in self.satellites)

    def __str__(self) -> str:
        return self.name


def process_data(task: str) -> dict[str, Object]:
    """Construct map from object name to object instance."""
    objects: dict[str, Object] = {}

    for line in task.strip().split("\n"):
        obj1_name, obj2_name = line.split(")")

        planet = objects.get(obj1_name, Object(obj1_name))
        satellite = objects.get(obj2_name, Object(obj2_name))

        planet.satellites.append(satellite)

        objects[obj1_name] = planet
        objects[obj2_name] = satellite

    return objects


def solve(task: str) -> int:
    """Find the number of direct and indirect orbits."""
    orbit_map = process_data(task)
    return orbit_map["COM"].traverse()
