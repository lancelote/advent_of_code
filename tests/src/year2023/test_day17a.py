"""2023 - Day 17 Part 1: Clumsy Crucible"""

from textwrap import dedent

from src.year2023.day17a import solve


def test_solve_simple0():
    task = dedent(
        r"""
        19
        21
        """
    ).strip()
    assert solve(task) == 3


def test_solve_simple1():
    task = dedent(
        r"""
        19111
        19191
        11191
        """
    ).strip()
    assert solve(task) == 10


def test_solve_simple2():
    task = dedent(
        r"""
        241343
        321545
        """
    ).strip()
    assert solve(task) == 20


def test_solve_simple3():
    task = dedent(
        r"""
        241343231
        321545535
        """
    ).strip()
    assert solve(task) == 34


def test_solve():
    task = dedent(
        r"""
        2413432311323
        3215453535623
        3255245654254
        3446585845452
        4546657867536
        1438598798454
        4457876987766
        3637877979653
        4654967986887
        4564679986453
        1224686865563
        2546548887735
        4322674655533
        """
    ).strip()
    assert solve(task) == 102
