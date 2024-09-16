"""2023 - Day 13 Part 2: Point of Incidence"""

from textwrap import dedent

from src.year2023.day13b import solve


def test_solve():
    task = dedent(
        """
        #.##..##.
        ..#.##.#.
        ##......#
        ##......#
        ..#.##.#.
        ..##..##.
        #.#.##.#.

        #...##..#
        #....#..#
        ..##..###
        #####.##.
        #####.##.
        ..##..###
        #....#..#
        """
    ).strip()
    assert solve(task) == 400
