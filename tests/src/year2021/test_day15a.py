"""2021 - Day 15 Part 1: Chiton."""

from textwrap import dedent

import pytest

from src.year2021.day15a import solve


@pytest.mark.parametrize(
    "task,risk",
    [
        (
            """
            1163751742
            1381373672
            2136511328
            3694931569
            7463417111
            1319128137
            1359912421
            3125421639
            1293138521
            2311944581
            """,
            40,
        ),
        (
            """
            19111
            19191
            11191
            """,
            10,
        ),
        (
            """
            12
            11
            """,
            2,
        ),
    ],
)
def test_solve(task, risk):
    task = dedent(task).strip()
    assert solve(task) == risk
