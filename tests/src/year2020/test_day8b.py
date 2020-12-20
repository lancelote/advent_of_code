"""2020 - Day 8 Part 2: Handheld Halting."""
from textwrap import dedent

from src.year2020.day8b import solve


def test_solve():
    task = dedent(
        """
        nop +0
        acc +1
        jmp +4
        acc +3
        jmp -3
        acc -99
        acc +1
        jmp -4
        acc +6
        """
    )
    assert solve(task) == 8
