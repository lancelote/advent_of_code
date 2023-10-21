"""2022 - Day 17 Part 1: Pyroclastic Flow."""
from src.year2022.day17a import solve


def test_solve():
    task = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"
    assert solve(task) == 3068
