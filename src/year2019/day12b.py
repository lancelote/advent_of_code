from __future__ import annotations

from math import gcd

from src.year2019.day12a import System


def lcd(x: int, y: int, z: int) -> int:
    return abs(x*y*z) // gcd(gcd(x, y), z)


def steps_until_repeat(system: System) -> int:
    base_xs = system.snapshot_x
    system.step()

    while system.snapshot_x != base_xs:
        system.step()

    return system.steps


def solve(task: str) -> int:
    system = System.from_raw_data(task)
    return steps_until_repeat(system)
