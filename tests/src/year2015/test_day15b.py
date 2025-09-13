"""2015 - Day 15 Part 2: Science for Hungry People."""

from src.year2015.day15b import solve


def test_solve():
    task = """Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3"""
    assert solve(task) == 57600000
