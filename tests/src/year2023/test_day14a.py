"""2023 - Day 14 Part 1: Parabolic Reflector Dish"""
from textwrap import dedent

from src.year2023.day14a import solve


def test_solve():
    task = dedent(
        """
        O....#....
        O.OO#....#
        .....##...
        OO.#O....O
        .O.....O#.
        O.#..O.#.#
        ..O..#O..O
        .......O..
        #....###..
        #OO..#....
        """
    ).strip()
    assert solve(task) == 136
