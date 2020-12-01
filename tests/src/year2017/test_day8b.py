"""2017 - Day 8 Part 2: I Heard You Like Registers tests."""

from src.year2017.day8b import solve


def test_solve():
    data = (
        "b inc 5 if a > 1\n"
        "a inc 1 if b < 5\n"
        "c dec -10 if a >= 1\n"
        "c inc -20 if c == 10\n"
    )
    assert solve(data) == 10
