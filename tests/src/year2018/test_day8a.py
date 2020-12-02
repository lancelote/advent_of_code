"""2018 - Day 8 Part 1: Memory Maneuver tests."""
from src.year2018.day8a import solve


def test_solve():
    sample_task = "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"
    assert solve(sample_task) == 138
