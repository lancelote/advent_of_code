"""2023 - Day 16 Part 2: The Floor Will Be Lava"""

from textwrap import dedent

from src.year2023.day16b import solve


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
    assert solve(task) == 51
