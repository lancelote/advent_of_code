"""2015 - Day 16 Part 2: Aunt Sue."""

from src.year2015.day16b import solve


def test_solve():
    task = """Sue 1: children: 1
Sue 2: children: 3, perfumes: 8,
Sue 3: cats: 8, pomeranians: 2, perfumes: 1"""
    assert solve(task) == 3
