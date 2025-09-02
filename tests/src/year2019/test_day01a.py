"""2019 - Day 1 Part 1: The Tyranny of the Rocket Equation."""

import pytest

from src.year2019.day01a import count_fuel
from src.year2019.day01a import process_data


def test_process_data():
    test_data = "12\n14\n1969\n100756"
    assert process_data(test_data) == [12, 14, 1969, 100756]


@pytest.mark.parametrize(
    "mass,fuel",
    [
        (12, 2),
        (14, 2),
        (1969, 654),
        (100756, 33583),
    ],
)
def test_count_fuel(mass, fuel):
    assert count_fuel(mass) == fuel
