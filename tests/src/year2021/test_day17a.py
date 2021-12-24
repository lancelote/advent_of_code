"""2021 - Day 17 Part 1: Trick Shot."""
from src.year2021.day17a import solve
from src.year2021.day17a import Target


def test_target_from_line():
    target = Target.from_line("target area: x=20..30, y=-10..-5")
    assert target.left_x == 20
    assert target.right_x == 30
    assert target.bottom_y == -10
    assert target.top_y == -5


def test_solve():
    assert solve("target area: x=20..30, y=-10..-5") == 45
