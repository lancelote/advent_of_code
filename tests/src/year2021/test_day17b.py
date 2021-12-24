"""2021 - Day 17 Part 2: Trick Shot."""
from src.year2021.day17b import solve


def test_solve():
    assert solve("target area: x=20..30, y=-10..-5") == 112
