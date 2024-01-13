"""2023 - Day 16 Part 2: The Floor Will Be Lava"""
from src.year2023.day16a import Beam
from src.year2023.day16a import count_energized
from src.year2023.day16a import Direction


def solve(task: str) -> int:
    layout = task.splitlines()

    rows = len(layout)
    cols = len(layout[0])

    starts: list[Beam] = []

    for r in range(rows):
        starts.append((Direction.E, (r, 0)))
        starts.append((Direction.W, (r, cols - 1)))

    for c in range(cols):
        starts.append((Direction.S, (0, c)))
        starts.append((Direction.N, (rows - 1, c)))

    return max(count_energized(start, layout) for start in starts)
