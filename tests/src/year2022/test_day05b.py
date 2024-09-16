"""2022 - Day 5 Part 2: Supply Stacks."""

from textwrap import dedent

from src.year2022.day05b import solve


def test_solve():
    task = dedent(
        """
            [D]
        [N] [C]
        [Z] [M] [P]
         1   2   3

        move 1 from 2 to 1
        move 3 from 1 to 3
        move 2 from 2 to 1
        move 1 from 1 to 2
        """
    )
    assert solve(task) == "MCD"
