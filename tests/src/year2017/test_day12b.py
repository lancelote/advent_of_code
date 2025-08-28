"""2017 - Day 12 Part 2: Digital Plumber tests."""

from src.year2017.day12b import solve


def test_solve():
    data = "0 <-> 2\n1 <-> 1\n2 <-> 0, 3, 4\n3 <-> 2, 4\n4 <-> 2, 3, 6\n5 <-> 6\n6 <-> 4, 5\n"
    assert solve(data) == 2
