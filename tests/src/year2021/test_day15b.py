"""2021 - Day 15 Part 1: Chiton."""
from textwrap import dedent

from src.year2021.day15b import solve


def test_solve():
    task = dedent(
        """
        1163751742
        1381373672
        2136511328
        3694931569
        7463417111
        1319128137
        1359912421
        3125421639
        1293138521
        2311944581
        """
    ).strip()
    assert solve(task) == 315
