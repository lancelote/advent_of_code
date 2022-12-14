"""2022 - Day 12 Part 1: Hill Climbing Algorithm."""
from collections.abc import Iterator
from typing import TypeAlias

HeightMap: TypeAlias = list[list[int]]
Square: TypeAlias = tuple[int, int]

SHIFTS = (
    (-1, 0),
    (0, +1),
    (+1, 0),
    (0, -1),
)


def construct_heightmap(task: str) -> HeightMap:
    heightmap: HeightMap = []

    for line in task.splitlines():
        row: list[int] = []

        for x in line:
            if x == "S":
                row.append(0)
            elif x == "E":
                row.append(25)
            else:
                row.append(ord(x) - 97)

        heightmap.append(row)

    return heightmap


def find(target: str, task: str) -> Square:
    for r, line in enumerate(task.splitlines()):
        for c, x in enumerate(line):
            if x == target:
                return r, c
    raise ValueError("start not found")


def neighbors(square: Square, heightmap: HeightMap) -> Iterator[Square]:
    assert heightmap
    assert heightmap[0]

    rows = len(heightmap)
    cols = len(heightmap[0])

    r, c = square

    for dr, dc in SHIFTS:
        nr = r + dr
        nc = c + dc

        if 0 <= nr < rows and 0 <= nc < cols:
            current_height = heightmap[r][c]
            new_height = heightmap[nr][nc]

            if new_height - current_height <= 1:
                yield nr, nc


def bfs(start: Square, end: Square, heightmap: HeightMap) -> int:
    visited: set[Square] = set()
    to_visit: list[Square] = [start]
    step = 0

    while to_visit:
        new_to_visit: list[Square] = []

        for square in to_visit:
            if square in visited:
                continue

            if square == end:
                return step

            visited.add(square)
            for neighbor in neighbors(square, heightmap):
                new_to_visit.append(neighbor)

        to_visit = new_to_visit
        step += 1

    raise ValueError("path not found")


def solve(task: str) -> int:
    heightmap = construct_heightmap(task)
    start = find("S", task)
    end = find("E", task)
    return bfs(start, end, heightmap)
