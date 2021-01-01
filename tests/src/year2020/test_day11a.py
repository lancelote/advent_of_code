"""2020 - Day 11 Part 1: Seating System."""
from textwrap import dedent

import pytest

from src.year2020.day11a import count_adjacent
from src.year2020.day11a import generate_next
from src.year2020.day11a import Matrix
from src.year2020.day11a import solve


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
    first_step = generate_next(task_matrix, 4, count_adjacent)
    assert first_step == first_step_expected

    second_step_expected = Matrix.from_task(
        dedent(
            """
            #.LL.L#.##
            #LLLLLL.L#
            L.L.L..L..
            #LLL.LL.L#
            #.LL.LL.LL
            #.LLLL#.##
            ..L.L.....
            #LLLLLLLL#
            #.LLLLLL.L
            #.#LLLL.##
            """
        )
    )
    second_step = generate_next(first_step, 4, count_adjacent)
    assert second_step == second_step_expected


def test_solve(task):
    assert solve(task) == 37
