"""2020 - Day 15 Part 2: Rambunctious Recitation."""

import pytest

from src.year2020.day15b import solve


@pytest.mark.skip("too slow")
@pytest.mark.parametrize(
    "task,expected_last",
    [
        ("0,3,6", 175594),
        ("1,3,2", 2578),
        ("2,1,3", 3544142),
        ("1,2,3", 261214),
        ("2,3,1", 6895259),
        ("3,2,1", 18),
        ("3,1,2", 362),
    ],
)
def test_solve(task, expected_last):
    assert solve(task) == expected_last
