"""2023 - Day 15 Part 2: Lens Library"""

from textwrap import dedent

from src.year2023.day15b import solve


def test_solve():
    task = dedent(
        """
        rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7
        """
    ).strip()
    assert solve(task) == 145
