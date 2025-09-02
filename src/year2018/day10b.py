"""2018 - Day 10 Part 2: The Stars Align."""

from src.year2018.day10a import Point
from src.year2018.day10a import Sky


def solve(task: str) -> int:
    """Count the number of seconds before the message will appear."""
    points = Point.parse_task(task)
    sky = Sky(points)
    seconds = sky.move_till_min_area()
    return seconds
