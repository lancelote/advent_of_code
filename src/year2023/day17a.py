"""2023 - Day 17 Part 1: Clumsy Crucible"""
import sys
from enum import Enum
from functools import cache
from typing import TypeAlias

Location: TypeAlias = tuple[int, int]
Path: TypeAlias = int
HeatLoss: TypeAlias = int


class Direction(Enum):
    N = 0
    E = 1
    S = 2
    W = 3


SHIFTS = {
    (-1, 0, Direction.N),
    (0, +1, Direction.E),
    (+1, 0, Direction.S),
    (0, -1, Direction.W),
}


REVERSE_DIRECTION = {
    Direction.N: {(+1, 0, Direction.S)},
    Direction.S: {(-1, 0, Direction.N)},
    Direction.E: {(0, -1, Direction.W)},
    Direction.W: {(0, +1, Direction.E)},
}


def solve(task: str) -> int:
    city = [[int(x) for x in line] for line in task.splitlines()]

    rows = len(city)
    cols = len(city[0])

    min_heat_loss = sys.maxsize
    goal = (rows - 1, cols - 1)

    visited = {(0, 0)}

    @cache
    def dfs(p: tuple[Location, Path, HeatLoss, Direction]) -> None:
        nonlocal min_heat_loss

        loc, path, heat, direction = p
        r, c = loc

        for dr, dc, new_dir in SHIFTS - REVERSE_DIRECTION[direction]:
            nr = r + dr
            nc = c + dc

            # we are out of bounds
            if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                continue

            new_path = (path + 1) if direction == new_dir else 1
            new_heat = heat + city[nr][nc]

            if new_path > 3:
                continue

            # we are on target
            if (nr, nc) == goal:
                min_heat_loss = min(min_heat_loss, new_heat)
                continue

            # no point searching further this path
            if new_heat > min_heat_loss:
                continue

            if (nr, nc) not in visited:
                visited.add((nr, nc))
                dfs(((nr, nc), new_path, new_heat, new_dir))
                visited.remove((nr, nc))

    dfs(((0, 1), 1, city[0][1], Direction.E))
    dfs(((1, 0), 1, city[1][0], Direction.S))

    return min_heat_loss
