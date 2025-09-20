"""2015 - Day 18 Part 1: Like a GIF For Your Yard."""

from src.year2015.day18a import count_on
from src.year2015.day18a import process_data
from src.year2015.day18a import solve
from src.year2015.day18a import step
from src.year2015.day18a import toggle

TASK = """.#.#.#
...##.
#....#
..#...
#.#..#
####.."""


def test_step():
    grid = process_data(TASK)

    assert count_on(grid) == 15

    grid = step(grid, toggle)

    assert count_on(grid) == 11

    grid = step(grid, toggle)

    assert count_on(grid) == 8

    grid = step(grid, toggle)

    assert count_on(grid) == 4

    grid = step(grid, toggle)

    assert count_on(grid) == 4


def test_solve():
    assert solve(TASK) == 4
