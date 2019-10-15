"""2017 - Day 12 Part 2: Digital Plumber tests."""

from src.year2017.day12b import solve


def test_solve():
    data = '0 <-> 2\n' \
           '1 <-> 1\n' \
           '2 <-> 0, 3, 4\n' \
           '3 <-> 2, 4\n' \
           '4 <-> 2, 3, 6\n' \
           '5 <-> 6\n' \
           '6 <-> 4, 5\n'
    assert solve(data) == 2
