"""2023 - Day 17 Part 1: Clumsy Crucible"""
from __future__ import annotations

import heapq
import sys
from enum import Enum
from typing import TypeAlias

Location: TypeAlias = tuple[int, int]
HeatLoss: TypeAlias = int
Path: TypeAlias = int


class Direction(Enum):
    B = 0  # base
    N = 1
    E = 2
    S = 3
    W = 4

    def __lt__(self, other: Direction) -> bool:
        return self.value < other.value


Point: TypeAlias = tuple[HeatLoss, Location, Direction]


SHIFTS = {
    (-1, 0, Direction.N),
    (0, +1, Direction.E),
    (+1, 0, Direction.S),
    (0, -1, Direction.W),
}

REVERSE_DIRECTION = {
    Direction.B: Direction.B,
    Direction.N: Direction.S,
    Direction.S: Direction.N,
    Direction.E: Direction.W,
    Direction.W: Direction.E,
}


def get_least_loss_path(
    city: list[list[int]],
    min_path: int = 1,
    max_path: int = 3,
) -> int:
    rows = len(city)
    cols = len(city[0])

    min_heat_loss = sys.maxsize
    goal = (rows - 1, cols - 1)

    seen: set[tuple[Location, Direction, Path]] = set()

    h: list[Point] = []
    heapq.heappush(h, (0, (0, 0), Direction.B))

    while h:
        heat, (r, c), direction = heapq.heappop(h)

        if heat > min_heat_loss:
            continue

        if (r, c) == goal:
            min_heat_loss = min(min_heat_loss, heat)
            continue

        reverse_dir = REVERSE_DIRECTION[direction]
        shifts = [s for s in SHIFTS if s[-1] not in {direction, reverse_dir}]

        for dr, dc, new_dir in shifts:
            new_heat = heat

            for i in range(min_path, max_path + 1):
                nr = r + dr * i
                nc = c + dc * i

                # out of bounds
                if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                    break

                new_heat += city[nr][nc]

                if ((nr, nc), new_dir, i) in seen:
                    continue
                else:
                    heapq.heappush(h, (new_heat, (nr, nc), new_dir))
                    seen.add(((nr, nc), new_dir, i))

    return min_heat_loss


def solve(task: str) -> int:
    city = [[int(x) for x in line] for line in task.splitlines()]
    return get_least_loss_path(city)
