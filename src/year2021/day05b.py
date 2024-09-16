"""2021 - Day 5 Part 2: Hydrothermal Venture."""

from src.year2021.day05a import Floor
from src.year2021.day05a import Segment


def solve(task: str) -> int:
    segments = [Segment.from_line(line) for line in task.splitlines()]

    floor = Floor()
    floor.draw(segments)

    return floor.num_overlap
