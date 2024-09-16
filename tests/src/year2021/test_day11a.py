"""2021 - Day 11 Part 1: Dumbo Octopus."""

from textwrap import dedent

from src.year2021.day11a import solve


def test_solve():
    task = dedent(
        """
        5483143223
        2745854711
        5264556173
        6141336146
        6357385478
        4167524645
        2176841721
        6882881134
        4846848554
        5283751526
        """
    ).strip()
    assert solve(task) == 1656
