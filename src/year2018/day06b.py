"""2018 - Day 6 Part 2: Chronal Coordinates."""
import math

from src.year2018.day06a import Grid as LegacyGrid


class Grid(LegacyGrid):
    """A gird of time dots with pins."""

    def calc_sum_distances(self) -> None:
        """Get sum of pin distances for each dot."""
        for pin in self.pins:
            for dot in self.dots:
                distance = pin - dot
                if dot.distance == math.inf:
                    dot.distance = distance
                else:
                    dot.distance += distance

    def closest_region_size(self, limit: int = 10000) -> int:
        """Get number of dots with distance less than limit."""
        total = 0
        self.calc_sum_distances()

        for dot in self.dots:
            if dot.distance < limit:
                total += 1
        return total


def solve(task: str, limit: int = 10000) -> int:
    """Find the size of the region with locations below the limit distance."""
    grid = Grid.parse_task(task)
    return grid.closest_region_size(limit)
