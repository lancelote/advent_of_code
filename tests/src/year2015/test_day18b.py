"""2015 - Day 18 Part 2: Like a GIF For Your Yard."""

from src.year2015.day18a import count_on
from src.year2015.day18a import process_data
from src.year2015.day18b import solve
from src.year2015.day18b import step
from src.year2015.day18b import toggle

TASK = """##.#.#
...##.
#....#
..#...
#.#..#
####.#"""


def test_step():
    grid = process_data(TASK)

    assert count_on(grid) == 17

    grid = step(grid, toggle)

    assert count_on(grid) == 18

    grid = step(grid, toggle)

    assert count_on(grid) == 18

    grid = step(grid, toggle)

    assert count_on(grid) == 18

    grid = step(grid, toggle)

    assert count_on(grid) == 14

    grid = step(grid, toggle)

    assert count_on(grid) == 17


def test_solve():
    assert solve(TASK) == 7
