"""2019 - Day 12 Part 1: The N-Body Problem."""

from __future__ import annotations

from itertools import permutations
from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class Moon:
    x: int
    y: int
    z: int

    dx: int = 0
    dy: int = 0
    dz: int = 0

    def apply_velocity(self):
        self.x += self.dx
        self.y += self.dy
        self.z += self.dz

    @classmethod
    def from_string(cls, string: str) -> Moon:
        x, y, z = [int(part[2:]) for part in string[1:-1].split(', ')]
        return cls(x, y, z)

    @property
    def coordinates(self) -> Tuple[int, int, int]:
        return self.x, self.y, self.z

    @property
    def velocity(self) -> Tuple[int, int, int]:
        return self.dx, self.dy, self.dz

    @property
    def potential_energy(self):
        return abs(self.x) + abs(self.y) + abs(self.z)
    
    @property
    def kinetic_energy(self):
        return abs(self.dx) + abs(self.dy) + abs(self.dz)

    @property
    def energy(self):
        return self.potential_energy * self.kinetic_energy


@dataclass
class System:
    moons: List[Moon]

    def apply_gravity(self):
        for moon1, moon2 in permutations(self.moons, 2):
            if moon1.x > moon2.x:
                moon1.dx -= 1
                moon2.dx += 1
            if moon1.y > moon2.y:
                moon1.dy -= 1
                moon2.dy += 1
            if moon1.z > moon2.z:
                moon1.dz -= 1
                moon2.dz += 1

    def apply_velocity(self):
        for moon in self.moons:
            moon.apply_velocity()

    def step(self):
        self.apply_gravity()
        self.apply_velocity()

    @classmethod
    def from_raw_data(cls, data: str) -> System:
        moons = [Moon.from_string(line) for line in data.strip().split('\n')]
        return cls(moons)

    @property
    def potential_energy(self):
        return sum(moon.potential_energy for moon in self.moons)
    
    @property
    def kinetic_energy(self):
        return sum(moon.kinetic_energy for moon in self.moons)

    @property
    def energy(self):
        return sum(moon.energy for moon in self.moons)


def solve(task: str) -> int:
    system = System.from_raw_data(task)
    for _ in range(1000):
        system.step()
    return system.energy
