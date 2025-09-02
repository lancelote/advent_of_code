"""2021 - Day 17 Part 2: Trick Shot."""

from src.year2021.day17a import Target
from src.year2021.day17a import Trajectory
from src.year2021.day17a import Velocity


def count_hit_trajectories(target: Target) -> int:
    count = 0

    for dx in range(target.right_x + 1):
        for dy in range(target.bottom_y, -target.bottom_y):
            velocity = Velocity(dx, dy)
            trajectory = Trajectory(velocity, target)
            trajectory.calculate()

            if trajectory.hit:
                count += 1

    return count


def solve(task: str) -> int:
    target = Target.from_line(task)
    return count_hit_trajectories(target)
