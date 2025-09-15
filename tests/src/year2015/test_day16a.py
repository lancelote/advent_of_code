"""2015 - Day 16 Part 1: Aunt Sue."""

from src.year2015.day16a import solve


def test_solve():
    task = """Sue 1: children: 1
Sue 2: children: 3, cats: 8,
Sue 3: cars: 2, perfumes: 1"""
    assert solve(task) == 3
