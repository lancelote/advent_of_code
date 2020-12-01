"""2017 - Day 11 Part 2: Hex Edh.

How many steps away is the furthest he ever got from his starting position?
"""

from src.year2017.day11a import SHIFTS


def solve(task: str) -> int:
    """Find furthest distance in hex grid.

    Relevant docs: https://www.redblobgames.com/grids/hexagons/
    """
    furthest = 0
    x, y, z = 0, 0, 0
    for direction in task.strip().split(","):
        dx, dy, dz = SHIFTS[direction]
        x += dx
        y += dy
        z += dz
        distance = max(abs(-x), abs(-y), abs(-z))
        if distance > furthest:
            furthest = distance
    return furthest
