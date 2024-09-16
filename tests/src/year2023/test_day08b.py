"""2023 - Day 8 Part 2: Haunted Wasteland"""

from textwrap import dedent

from src.year2023.day08b import solve


def test_solve():
    task = dedent(
        """
        LR

        11A = (11B, XXX)
        11B = (XXX, 11Z)
        11Z = (11B, XXX)
        22A = (22B, XXX)
        22B = (22C, 22C)
        22C = (22Z, 22Z)
        22Z = (22B, 22B)
        XXX = (XXX, XXX)
        """
    ).strip()
    assert solve(task) == 6
