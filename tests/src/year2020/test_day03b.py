"""2020 - Day 3 Part 2: Toboggan Trajectory."""

from textwrap import dedent

import pytest

from src.year2020.day03b import solve


@pytest.mark.parametrize(
    "task,expected",
    [
        (
            dedent(
                """
                ..##.......
                #...#...#..
                .#....#..#.
                ..#.#...#.#
                .#...##..#.
                ..#.##.....
                .#.#.#....#
                .#........#
                #.##...#...
                #...##....#
                .#..#...#.#
                """
            ),
            336,
        ),
    ],
)
def test_solve(task, expected):
    assert solve(task) == expected
