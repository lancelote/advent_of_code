"""2021 - Day 13 Part 1: Transparent Origami."""
from textwrap import dedent

from src.year2021.day13a import solve


def test_solve():
    task = dedent(
        """
        6,10
        0,14
        9,10
        0,3
        10,4
        4,11
        6,0
        6,12
        4,1
        0,13
        10,12
        3,4
        3,0
        8,4
        1,10
        2,14
        8,10
        9,0
        
        fold along y=7
        fold along x=5
        """
    ).strip()
    assert solve(task) == 17
