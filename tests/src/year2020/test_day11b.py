"""2020 - Day 11 Part 2: Seating System."""

from textwrap import dedent

import pytest

from src.year2020.day11a import Matrix
from src.year2020.day11a import generate_next
from src.year2020.day11b import count_visible
from src.year2020.day11b import solve


@pytest.fixture
def task():
    return dedent(
        """
        L.LL.LL.LL
        LLLLLLL.LL
        L.L.L..L..
        LLLL.LL.LL
        L.LL.LL.LL
        L.LLLLL.LL
        ..L.L.....
        LLLLLLLLLL
        L.LLLLLL.L
        L.LLLLL.LL
        """
    )


def test_steps(task):
    task_matrix = Matrix.from_task(task)
    first_step_expected = Matrix.from_task(
        dedent(
            """
            #.##.##.##
            #######.##
            #.#.#..#..
            ####.##.##
            #.##.##.##
            #.#####.##
            ..#.#.....
            ##########
            #.######.#
            #.#####.##
            """
        )
    )
    first_step = generate_next(task_matrix, 5, count_visible)
    assert first_step == first_step_expected

    second_step_expected = Matrix.from_task(
        dedent(
            """
            #.LL.LL.L#
            #LLLLLL.LL
            L.L.L..L..
            LLLL.LL.LL
            L.LL.LL.LL
            L.LLLLL.LL
            ..L.L.....
            LLLLLLLLL#
            #.LLLLLL.L
            #.LLLLL.L#
            """
        )
    )
    second_step = generate_next(first_step, 5, count_visible)
    assert second_step == second_step_expected


def test_solve(task):
    assert solve(task) == 26
