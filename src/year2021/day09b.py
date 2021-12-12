"""2021 - Day 9 Part 2: Smoke Basin."""
from collections import deque
from typing import Deque
from typing import Iterable
from typing import Iterator

from src.year2021.day09a import adjacent
from src.year2021.day09a import Heightmap
from src.year2021.day09a import lowest
from src.year2021.day09a import Point


def basins(low_points: Iterable[Point], heightmap: Heightmap) -> Iterator[int]:
    """Yields basin sizes."""
    for low_point in low_points:
        visited = {low_point}
        to_check: Deque[Point] = deque()
        to_check.append(low_point)

        while to_check:
            current = to_check.popleft()
            for neighbor in adjacent(current, heightmap):
                if neighbor.height == 9:
                    continue
                elif neighbor not in visited:
                    visited.add(neighbor)
                    to_check.append(neighbor)

        yield len(visited)


def solve(task: str) -> int:
    """Get top-3 basin sizes product."""
    heightmap = [
        [int(x) for x in list(line.strip())]
        for line in task.strip().split("\n")
    ]
    low_points = lowest(heightmap)
    basin_sizes = sorted(basins(low_points, heightmap), reverse=True)
    return basin_sizes[0] * basin_sizes[1] * basin_sizes[2]
