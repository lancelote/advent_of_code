"""2018 - Day 1 Part 2: Chronal Calibration tests."""

import pytest

from src.year2018.day01b import solve


@pytest.mark.parametrize(
    ("changes", "expected"),
    [
        ("+1\n-1", 0),
        ("+3\n+3\n+4\n-2\n-4", 10),
        ("-6\n+3\n+8\n+5\n-6", 5),
        ("+7\n+7\n-2\n-7\n-4", 14),
    ],
)
def test_solve(changes, expected):
    assert solve(changes) == expected
