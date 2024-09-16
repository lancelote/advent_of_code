"""2017 - Day 7 Part 2: Recursive Circus tests."""

import pytest

from src.year2017.day07b import find_unique
from src.year2017.day07b import solve


@pytest.mark.parametrize(
    ("items", "expected"),
    [
        ([2, 1, 1], (-1, 0)),
        ([0, 1, 1], (1, 0)),
        ([1, 1, 2], (-1, 2)),
        ([1, 1, 0], (1, 2)),
        ([1, 2, 1], (-1, 1)),
    ],
)
def test_find_unique(items, expected):
    assert find_unique(items) == expected


def test_solve():
    data = """
    pbga (66)
    xhth (57)
    ebii (61)
    havc (66)
    ktlj (57)
    fwft (72) -> ktlj, cntj, xhth
    qoyq (66)
    padx (45) -> pbga, havc, qoyq
    tknk (41) -> ugml, padx, fwft
    jptl (61)
    ugml (68) -> gyxo, ebii, jptl
    gyxo (61)
    cntj (57)
    """
    assert solve(data) == 60
