# pylint: disable=no-self-use

"""2017 - Day 5 Part 2: A Maze of Twisty Trampolines, All Alike tests."""

from src.year2017.day5b import solve


def test_solve():
    assert solve('0\n3\n0\n1\n-3') == 10
