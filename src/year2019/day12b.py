"""2019 - Day 12 Part 2: The N-Body Problem."""
from __future__ import annotations

from math import gcd

from src.year2019.day12a import System


def lcd(x: int, y: int) -> int:
    """Calculate least common divisor between x and y."""
    return abs(x * y) // gcd(x, y)


def steps_until_repeat(task: str) -> int:
    """Calculate number of steps to return to the same position."""
    # Calculate xs
    system = System.from_raw_data(task)
    base_xs = system.snapshot_x
    system.step()

    while system.snapshot_x != base_xs:
        system.step()

    x_steps = system.steps
    print(f"x steps {x_steps}")

    # Calculate ys
    system = System.from_raw_data(task)
    base_ys = system.snapshot_y
    system.step()

    while system.snapshot_y != base_ys:
        system.step()

    y_steps = system.steps
    print(f"y steps {y_steps}")

    # Calculate zs
    system = System.from_raw_data(task)
    base_zs = system.snapshot_z
    system.step()

    while system.snapshot_z != base_zs:
        system.step()

    z_steps = system.steps
    print(f"z steps {z_steps}")

    return lcd(lcd(x_steps, y_steps), z_steps)


def solve(task: str) -> int:
    """Find the number of steps to restore system to original state."""
    return steps_until_repeat(task)
