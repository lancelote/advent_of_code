"""2019 - Day 1 Part 2: The Tyranny of the Rocket Equation."""

from src.year2019.day01a import count_fuel, process_data


def solve(task: str) -> int:
    """Count total fuel requirements taking fuel mass into account."""
    total_fuel = 0

    for mass in process_data(task):
        while mass > 0:
            fuel = max(0, count_fuel(mass))
            total_fuel += fuel
            mass = fuel

    return total_fuel
