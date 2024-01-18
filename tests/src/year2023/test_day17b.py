"""2023 - Day 17 Part 2: Clumsy Crucible"""
from textwrap import dedent

from src.year2023.day17b import solve


def test_solve_simple():
    task = dedent(
        r"""
        111111111111
        999999999991
        999999999991
        999999999991
        999999999991
        """
    ).strip()
    assert solve(task) == 71


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
    assert solve(task) == 94
