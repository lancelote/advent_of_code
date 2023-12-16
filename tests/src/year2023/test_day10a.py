"""2023 - Day 10 Part 1: Pipe Maze"""
from textwrap import dedent

from src.year2023.day10a import solve


def test_solve_0():
    task = dedent(
        """
        .....
        .S-7.
        .|.|.
        .L-J.
        .....
        """
    ).strip()
    assert solve(task) == 4


def test_solve_1():
    task = dedent(
        """
        ..F7.
        .FJ|.
        SJ.L7
        |F--J
        LJ...
        """
    ).strip()
    assert solve(task) == 8
