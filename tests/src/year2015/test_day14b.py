"""2015 - Day 14 Part 2: Reindeer Olympics."""

from src.year2015.day14a import Reindeer
from src.year2015.day14b import max_points_after


def test_max_points_after():
    deers = [
        Reindeer(14, 10, 127),
        Reindeer(16, 11, 162),
    ]
    assert max_points_after(deers, 1000) == 689
