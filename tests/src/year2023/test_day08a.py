"""2023 - Day 8 Part 1: Haunted Wasteland"""

from textwrap import dedent

from src.year2023.day08a import solve


def test_solve():
    task = dedent(
        """
        RL

        AAA = (BBB, CCC)
        BBB = (DDD, EEE)
        CCC = (ZZZ, GGG)
        DDD = (DDD, DDD)
        EEE = (EEE, EEE)
        GGG = (GGG, GGG)
        ZZZ = (ZZZ, ZZZ)
        """
    ).strip()
    assert solve(task) == 2
