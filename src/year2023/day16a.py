"""2023 - Day 16 Part 1: The Floor Will Be Lava"""

import enum
from collections import deque
from typing import TypeAlias, assert_never


class Direction(enum.Enum):
    N = 0
    E = 1
    S = 2
    W = 3


C: TypeAlias = tuple[int, int]
Beam: TypeAlias = tuple[Direction, C]


def get_next_beams(beam: Beam, layout: list[str]) -> list[Beam]:
    rows = len(layout)
    cols = len(layout[0])

    beams: list[Beam] = []

    direction, (r, c) = beam
    tile = layout[r][c]

    match tile:
        case ".":
            match direction:
                case Direction.N:
                    nr, nc = r - 1, c
                case Direction.E:
                    nr, nc = r, c + 1
                case Direction.S:
                    nr, nc = r + 1, c
                case Direction.W:
                    nr, nc = r, c - 1
                case _:
                    assert_never(direction)
            beams.append((direction, (nr, nc)))
        case "|":
            match direction:
                case Direction.N:
                    beams.append((Direction.N, (r - 1, c)))
                case Direction.E | Direction.W:
                    beams.append((Direction.N, (r - 1, c)))
                    beams.append((Direction.S, (r + 1, c)))
                case Direction.S:
                    beams.append((Direction.S, (r + 1, c)))
                case _:
                    assert_never(direction)
        case "-":
            match direction:
                case Direction.N | Direction.S:
                    beams.append((Direction.E, (r, c + 1)))
                    beams.append((Direction.W, (r, c - 1)))
                case Direction.W:
                    beams.append((Direction.W, (r, c - 1)))
                case Direction.E:
                    beams.append((Direction.E, (r, c + 1)))
                case _:
                    assert_never(direction)

        case "/":
            match direction:
                case Direction.N:
                    beams.append((Direction.E, (r, c + 1)))
                case Direction.E:
                    beams.append((Direction.N, (r - 1, c)))
                case Direction.S:
                    beams.append((Direction.W, (r, c - 1)))
                case Direction.W:
                    beams.append((Direction.S, (r + 1, c)))
                case _:
                    assert_never(direction)
        case "\\":
            match direction:
                case Direction.N:
                    beams.append((Direction.W, (r, c - 1)))
                case Direction.E:
                    beams.append((Direction.S, (r + 1, c)))
                case Direction.S:
                    beams.append((Direction.E, (r, c + 1)))
                case Direction.W:
                    beams.append((Direction.N, (r - 1, c)))
                case _:
                    assert_never(direction)
        case _:
            raise ValueError

    return [b for b in beams if 0 <= b[1][0] < rows and 0 <= b[1][1] < cols]


def count_energized(start: Beam, layout: list[str]) -> int:
    energized: set[C] = set()
    visited: set[Beam] = set()
    to_visit: deque[Beam] = deque()
    to_visit.append(start)

    while to_visit:
        for _ in range(len(to_visit)):
            beam = to_visit.popleft()
            energized.add(beam[1])
            visited.add(beam)

            for next_beam in get_next_beams(beam, layout):
                if next_beam not in visited:
                    to_visit.append(next_beam)

    return len(energized)


def solve(task: str) -> int:
    layout = task.splitlines()
    return count_energized((Direction.E, (0, 0)), layout)
