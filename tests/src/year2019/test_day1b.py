"""2019 - Day 1 Part 2: The Tyranny of the Rocket Equation."""

import pytest

from src.year2019.day1b import solve


@pytest.mark.parametrize('task,total_fuel', [
    ('14', 2),
    ('1969', 966),
    ('100756', 50346),
])
def test_solve(task, total_fuel):
    assert solve(task) == total_fuel
