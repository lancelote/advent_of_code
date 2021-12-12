"""2020 - Day 3 Part 1: Toboggan Trajectory."""
from textwrap import dedent

import pytest

from src.year2020.day03a import solve


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
            7,
        ),
    ],
)
def test_solve(task, expected):
    assert solve(task) == expected
