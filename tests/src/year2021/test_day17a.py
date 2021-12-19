"""2021 - Day 17 Part 1: Trick Shot."""

from src.year2021.day17a import Target


def test_target_from_line():
    target = Target.from_line("target area: x=20..30, y=-10..-5")
    assert target.x_min == 20
    assert target.x_max == 30
    assert target.y_min == -10
    assert target.y_max == -5
