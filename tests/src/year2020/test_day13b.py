"""2020 - Day 13 Part 2: Shuttle Search."""

import pytest

from src.year2020.day13b import solve


@pytest.mark.parametrize(
    "task,expected",
    [
        ("_\n7,13,x,x,59,x,31,19", 1068781),
        ("_\n17,x,13,19", 3417),
        ("_\n67,7,59,61", 754018),
        ("_\n67,x,7,59,61", 779210),
        ("_\n67,7,x,59,61", 1261476),
        ("_\n1789,37,47,1889", 1202161486),
    ],
)
def test_solve(task, expected):
    assert solve(task) == expected
