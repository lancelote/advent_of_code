"""2021 - Day 11 Part 1: Dumbo Octopus."""
from __future__ import annotations

from collections import deque
from typing import Deque
from typing import Iterator

SHIFTS = [
    (-1, -1),
    (-1, 0),
    (-1, +1),
    (0, +1),
    (+1, +1),
    (+1, 0),
    (+1, -1),
    (0, -1),
]


class Octopus:
    def __init__(self, i: int, j: int, energy: int) -> None:
        self.i = i
        self.j = j
        self.energy = energy

    def gain_energy(self) -> None:
        self.energy += 1
        self.energy %= 10


class Data:
    def __init__(self, data: list[list[Octopus]]) -> None:
        self.data = data

    @classmethod
    def from_task(cls, task: str) -> Data:
        return Data(
            [
                [Octopus(i, j, int(energy)) for j, energy in enumerate(line)]
                for i, line in enumerate(task.splitlines())
            ]
        )

    @property
    def all_zeros(self) -> bool:
        return all(x.energy == 0 for line in self.data for x in line)

    def iter_adjacent_to(self, octopus: Octopus) -> Iterator[Octopus]:
        for di, dj in SHIFTS:
            new_i = octopus.i + di
            new_j = octopus.j + dj

            valid_new_i = 0 <= new_i < 10
            valid_new_j = 0 <= new_j < 10

            if valid_new_i and valid_new_j:
                yield self.data[new_i][new_j]

    def print(self) -> None:
        for line in self.data:
            print("".join(str(x.energy) for x in line))

    def __iter__(self) -> Iterator[list[Octopus]]:
        return self.data.__iter__()


def make_step(data: Data) -> int:
    flashes = 0
    to_flash: Deque[Octopus] = deque()

    # increase everyone's energy
    for line in data:
        for octopus in line:
            octopus.gain_energy()
            if octopus.energy == 0:
                to_flash.append(octopus)

    # flash
    while to_flash:
        flashes += 1
        octopus = to_flash.popleft()

        for neighbor in data.iter_adjacent_to(octopus):
            if neighbor.energy != 0:
                neighbor.gain_energy()
                if neighbor.energy == 0:
                    to_flash.append(neighbor)

    return flashes


def solve(task: str) -> int:
    data = Data.from_task(task)
    flashes = 0

    for _ in range(100):
        flashes += make_step(data)

    return flashes
