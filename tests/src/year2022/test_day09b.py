"""2022 - Day 9 Part 2: Rope Bridge."""
from textwrap import dedent

from src.year2022.day09b import solve


def test_solve_1():
    task = dedent(
        """
        R 4
        U 4
        L 3
        D 1
        R 4
        D 1
        L 5
        R 2
        """
    ).strip()
    assert solve(task) == 1


def test_solve_2():
    task = dedent(
        """
        R 5
        U 8
        L 8
        D 3
        R 17
        D 10
        L 25
        U 20
        """
    ).strip()
    assert solve(task) == 36
