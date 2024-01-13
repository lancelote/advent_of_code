"""2023 - Day 16 Part 1: The Floor Will Be Lava"""
from textwrap import dedent

from src.year2023.day16a import solve


def test_solve():
    task = dedent(
        r"""
        .|...\....
        |.-.\.....
        .....|-...
        ........|.
        ..........
        .........\
        ..../.\\..
        .-.-/..|..
        .|....-|.\
        ..//.|....
        """
    ).strip()
    assert solve(task) == 46
