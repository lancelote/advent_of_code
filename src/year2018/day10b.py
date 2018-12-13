"""2018 - Day 10 Part 2: The Stars Align.

Good thing you didn't have to wait, because that would have taken a long time
- much longer than the 3 seconds in the example above.

Impressed by your sub-hour communication capabilities, the Elves are curious:
exactly how many seconds would they have needed to wait for that message to
appear?
"""

from src.year2018.day10a import Point, Sky


def solve(task: str) -> int:
    """Count the number of seconds before the message will appear."""
    points = Point.parse_task(task)
    sky = Sky(points)
    seconds = sky.move_till_min_area()
    return seconds
