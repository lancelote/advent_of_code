"""2024 - Day 11 Part 1: Plutonian Pebbles"""

from src.year2024.day11a import solve


def test_solve():
    task = "125 17"
    assert solve(task) == 55312
