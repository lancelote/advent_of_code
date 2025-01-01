"""2024 - Day 16 Part 1: Reindeer Maze"""

import sys
from collections import deque
from enum import StrEnum

sys.setrecursionlimit(10_000)


class Direction(StrEnum):
    NORTH = "N"
    EAST = "E"
    SOUTH = "S"
    WEST = "W"


SHIFTS = {
    # dr rc
    Direction.NORTH: (-1, 0),
    Direction.EAST: (0, +1),
    Direction.SOUTH: (+1, 0),
    Direction.WEST: (0, -1),
}

TO_LEFT = {
    Direction.NORTH: Direction.WEST,
    Direction.WEST: Direction.SOUTH,
    Direction.SOUTH: Direction.EAST,
    Direction.EAST: Direction.NORTH,
}

TO_RIGHT = {
    Direction.NORTH: Direction.EAST,
    Direction.EAST: Direction.SOUTH,
    Direction.SOUTH: Direction.WEST,
    Direction.WEST: Direction.NORTH,
}


def solve(task: str) -> int:
    data = [list(line) for line in task.split("\n")]

    rows = len(data)
    cols = len(data[0])

    start_r, start_c = rows - 2, 1
    end_r, end_c = 1, cols - 2

    to_process: deque[tuple[int, int, int, Direction]] = deque()
    best_score: dict[tuple[int, int, Direction], int] = {}

    to_process.append((start_r, start_c, 0, Direction.EAST))
    best_score[(start_r, start_c, Direction.EAST)] = 0

    result = sys.maxsize

    while to_process:
        r, c, score, direction = to_process.popleft()

        if score >= result:
            continue

        if r == end_r and c == end_c:
            result = min(result, score)
            continue

        if not (0 <= r < rows and 0 <= c < cols):
            continue

        if data[r][c] == "#":
            continue

        if (r, c, direction) in best_score:
            old_score = best_score[(r, c, direction)]
            if old_score < score:
                continue

        best_score[(r, c, direction)] = score

        dr, dc = SHIFTS[direction]
        to_process.append((r + dr, c + dc, score + 1, direction))
        to_process.append((r, c, score + 1000, TO_LEFT[direction]))
        to_process.append((r, c, score + 1000, TO_RIGHT[direction]))

    return result
