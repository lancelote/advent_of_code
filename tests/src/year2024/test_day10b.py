"""2024 - Day 10 Part 2: Hoof It"""

from textwrap import dedent

from src.year2024.day10b import solve


def test_solve():
    task = dedent(
        """
        89010123
        78121874
        87430965
        96549874
        45678903
        32019012
        01329801
        10456732
        """
    ).strip()
    assert solve(task) == 81
