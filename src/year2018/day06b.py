"""2018 - Day 6 Part 2: Chronal Coordinates.

On the other hand, if the coordinates are safe, maybe the best you can do is
try to find a region near as many coordinates as possible.

For example, suppose you want the sum of the Manhattan distance to all of the
coordinates to be less than 32. For each location, add up the distances to all
of the given coordinates; if the total of those distances is less than 32, that
location is within the desired region. Using the same coordinates as above, the
resulting region looks like this:

    ..........
    .A........
    ..........
    ...###..C.
    ..#D###...
    ..###E#...
    .B.###....
    ..........
    ..........
    ........F.

In particular, consider the highlighted location 4,3 located at the top middle
of the region. Its calculation is as follows, where abs() is the absolute value
function:

    Distance to coordinate A: abs(4-1) + abs(3-1) =  5
    Distance to coordinate B: abs(4-1) + abs(3-6) =  6
    Distance to coordinate C: abs(4-8) + abs(3-3) =  4
    Distance to coordinate D: abs(4-3) + abs(3-4) =  2
    Distance to coordinate E: abs(4-5) + abs(3-5) =  3
    Distance to coordinate F: abs(4-8) + abs(3-9) = 10
    Total distance: 5 + 6 + 4 + 2 + 3 + 10 = 30

Because the total distance to all coordinates (30) is less than 32, the
location is within the region.

This region, which also includes coordinates D and E, has a total size of 16.

Your actual region will need to be much larger than this example, though,
instead including all locations with a total distance of less than 10000.

What is the size of the region containing all locations which have a total
distance to all given coordinates of less than 10000?
"""
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
