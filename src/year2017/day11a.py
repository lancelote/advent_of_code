r"""2017 - Day 11 Part 1: Hex Edh."""

SHIFTS = {
    "n": (0, 1, -1),
    "ne": (1, 0, -1),
    "se": (1, -1, 0),
    "s": (0, -1, 1),
    "sw": (-1, 0, 1),
    "nw": (-1, 1, 0),
}


def solve(task: str) -> int:
    """Find shortest distance in hex grid.

    Relevant docs: https://www.redblobgames.com/grids/hexagons/
    """
    x, y, z = 0, 0, 0
    for direction in task.strip().split(","):
        dx, dy, dz = SHIFTS[direction]
        x += dx
        y += dy
        z += dz
    return max(abs(-x), abs(-y), abs(-z))
