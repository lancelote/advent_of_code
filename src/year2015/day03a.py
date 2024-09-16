"""2015 - Day 3 Part 1: Perfectly Spherical Houses in a Vacuum."""

from collections import defaultdict

SHIFT = {
    "<": (-1, 0),
    "^": (0, 1),
    ">": (1, 0),
    "v": (0, -1),
}


def visit_houses(task: str) -> dict[tuple[int, int], int]:
    x, y = 0, 0
    visited_houses = defaultdict(int)
    visited_houses[(0, 0)] = 1

    for direction in task:
        dx, dy = SHIFT[direction]
        x -= dx
        y -= dy
        visited_houses[(x, y)] += 1

    return visited_houses


def solve(task: str) -> int:
    visited_houses = visit_houses(task)
    return len(visited_houses)
