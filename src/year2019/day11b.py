"""2019 - Day 11 Part 2: Space Police."""

from src.year2019.day11a import Hull, Robot, Coordinates, Color, Panel


def solve(task: str) -> int:
    """Print the painted whole."""
    hull = Hull(Panel)
    start_panel = hull[Coordinates(0, 0)]
    start_panel.paint(Color.WHITE)

    robot = Robot()
    robot.load_program(task)
    robot.paint(hull)

    hull.print()
    return -1
