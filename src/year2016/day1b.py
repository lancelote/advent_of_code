"""2016 - Day 1 Part 2: No Time for a Taxicab.

Then, you notice the instructions continue on the back of the Recruiting
Document. Easter Bunny HQ is actually at the first location you visit twice.

For example, if your instructions are R8, R4, R4, R8, the first location you
visit twice is 4 blocks away, due East.

How many blocks away is the first location you visit twice?
"""
from copy import copy
from typing import Generator
from typing import List

from src.year2016.day1a import Instruction
from src.year2016.day1a import Point
from src.year2016.day1a import processed_data
from src.year2016.day1a import update_direction


def in_between(start: Point, end: Point) -> Generator[Point, None, None]:
    """Generate points between start and end including end."""
    if start.x != end.x and start.y != end.y:
        raise ValueError("Points not belong to same horizontal or vertical")

    if start.x < end.x:  # East
        difference = end.x - start.x
        for i in range(1, difference + 1):
            yield Point(start.x + i, start.y)
    elif start.x > end.x:  # West
        difference = start.x - end.x
        for i in range(1, difference + 1):
            yield Point(start.x - i, start.y)
    elif start.y < end.y:  # North
        difference = end.y - start.y
        for i in range(1, difference + 1):
            yield Point(start.x, start.y + i)
    elif start.y > end.y:  # South
        difference = start.y - end.y
        for i in range(1, difference + 1):
            yield Point(start.x, start.y - i)
    else:
        raise ValueError("Start point equals to end point")


def solve(task: str) -> int:
    """Compute how many blocks away is Easter Bunny HQ."""
    direction = 0  # North
    current = Point()
    visited = [copy(current)]
    instructions = processed_data(task)  # type: List[Instruction]

    for instruction in instructions:
        direction = update_direction(direction, instruction.direction)
        previous = copy(current)
        current.move(direction, instruction.distance)
        for point in in_between(previous, current):
            if point in visited:
                return point.distance_from_zero()
            else:
                visited.append(point)
    raise ValueError("No points are visited twice")
