"""2017 - Day 5 Part 1: A Maze of Twisty Trampolines, All Alike tests."""

from src.year2017.day5a import solve


def test_solve_positive_jump():
    assert solve("0\n3\n0\n1\n-3\n") == 5


def test_solve_negative_jump():
    assert solve("0\n-3\n") == 3
