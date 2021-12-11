"""2021 - Day 11 Part 1: Dumbo Octopus."""
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


def step(data: Data) -> int:
    """Perform a single step by increasing energy and flashing octopuses."""
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
    data = Data(
        [
            [Octopus(i, j, int(energy)) for j, energy in enumerate(line)]
            for i, line in enumerate(task.splitlines())
        ]
    )
    flashes = 0

    for _ in range(100):
        flashes += step(data)

    return flashes
