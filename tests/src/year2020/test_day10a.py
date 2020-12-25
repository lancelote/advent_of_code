"""2020 - Day 10 Part 1: Adapter Array."""
from textwrap import dedent

import pytest

from src.year2020.day10a import solve


@pytest.mark.parametrize(
    "task,answer",
    [
        (
            dedent(
                """
            16
            10
            15
            5
            1
            11
            7
            19
            6
            12
            4
            """
            ),
            7 * 5,
        ),
        (
            dedent(
                """
            28
            33
            18
            42
            31
            14
            46
            20
            48
            47
            24
            23
            49
            45
            19
            38
            39
            11
            1
            32
            25
            35
            8
            17
            7
            9
            4
            2
            34
            10
            3
            """
            ),
            22 * 10,
        ),
    ],
)
def test_solve(task, answer):
    assert solve(task) == answer
