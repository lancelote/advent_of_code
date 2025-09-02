"""2017 - Day 12 Part 2: Digital Plumber tests."""

from src.year2017.day12b import solve


def test_solve():
    data = """0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5
"""
    assert solve(data) == 2
