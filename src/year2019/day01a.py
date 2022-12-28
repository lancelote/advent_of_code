"""2019 - Day 1 Part 1: The Tyranny of the Rocket Equation."""


def count_fuel(mass: int) -> int:
    """Compute full need for a module with a given mass."""
    return mass // 3 - 2


def process_data(data: str) -> list[int]:
    """Convert raw data to a list of modules masses."""
    return [int(line) for line in data.strip().split("\n")]


def solve(task: str) -> int:
    """Sum fuel required for each module."""
    return sum(count_fuel(mass) for mass in process_data(task))
