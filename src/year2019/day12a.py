"""2019 - Day 12 Part 1: The N-Body Problem."""

from __future__ import annotations

from dataclasses import dataclass
from itertools import permutations


@dataclass
class Moon:
    """Moon representation: Io, Europa, Ganymede or Callisto."""

    x: int
    y: int
    z: int

    dx: int = 0
    dy: int = 0
    dz: int = 0

    def apply_velocity(self) -> None:
        """Add velocity to coordinates."""
        self.x += self.dx
        self.y += self.dy
        self.z += self.dz

    @classmethod
    def from_string(cls, string: str) -> Moon:
        """Create Moon instance from raw data: e.g. "<x=1, y=3, z=-11>"."""
        x, y, z = (int(part[2:]) for part in string[1:-1].split(", "))
        return cls(x, y, z)

    @property
    def coordinates(self) -> tuple[int, int, int]:
        """Return moon coordinates in tuple for assessment."""
        return self.x, self.y, self.z

    @property
    def velocity(self) -> tuple[int, int, int]:
        """Return moon velocities in tuple for assessment."""
        return self.dx, self.dy, self.dz

    @property
    def potential_energy(self) -> int:
        """Calculate moon potential energy."""
        return abs(self.x) + abs(self.y) + abs(self.z)

    @property
    def kinetic_energy(self) -> int:
        """Calculate moon kinetic energy."""
        return abs(self.dx) + abs(self.dy) + abs(self.dz)

    @property
    def energy(self) -> int:
        """Calculate moon total energy."""
        return self.potential_energy * self.kinetic_energy


@dataclass
class System:
    """System of a number of moons."""

    moons: list[Moon]
    steps: int = 0

    def apply_gravity(self) -> None:
        """Apply gravity to each moon in system."""
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

    def apply_velocity(self) -> None:
        """Apply velocity to each moon in system."""
        for moon in self.moons:
            moon.apply_velocity()

    def step(self) -> None:
        """Make a step in system simulation."""
        self.steps += 1
        self.apply_gravity()
        self.apply_velocity()

    @classmethod
    def from_raw_data(cls, data: str) -> System:
        """Convert raw data to a System instance.

        Data example:

            <x=1, y=3, z=-11>
            <x=17, y=-10, z=-8>
            <x=-1, y=-15, z=2>
            <x=12, y=-4, z=-4>
        """
        moons = [Moon.from_string(line) for line in data.strip().split("\n")]
        return cls(moons)

    @property
    def snapshot_x(self) -> list[tuple[int, int]]:
        """Get the snapshot of x coordinates."""
        return [(moon.x, moon.dx) for moon in self.moons]

    @property
    def snapshot_y(self) -> list[tuple[int, int]]:
        """Get the snapshot of y coordinates."""
        return [(moon.y, moon.dy) for moon in self.moons]

    @property
    def snapshot_z(self) -> list[tuple[int, int]]:
        """Get the snapshot of z coordinates."""
        return [(moon.z, moon.dz) for moon in self.moons]

    @property
    def potential_energy(self) -> int:
        """Calculate system potential energy."""
        return sum(moon.potential_energy for moon in self.moons)

    @property
    def kinetic_energy(self) -> int:
        """Calculate system kinetic energy."""
        return sum(moon.kinetic_energy for moon in self.moons)

    @property
    def energy(self) -> int:
        """Calculate system total energy."""
        return sum(moon.energy for moon in self.moons)


def solve(task: str) -> int:
    """Calculate total system energy after 1000 simulation steps."""
    system = System.from_raw_data(task)
    for _ in range(1000):
        system.step()
    return system.energy
