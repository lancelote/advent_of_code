"""2024 - Day 4 Part 2: Ceres Search"""

from textwrap import dedent

from src.year2024.day04b import solve


def test_solve():
    task = dedent(
        """
        .M.S......
        ..A..MSMS.
        .M.S.MAA..
        ..A.ASMSM.
        .M.S.M....
        ..........
        S.S.S.S.S.
        .A.A.A.A..
        M.M.M.M.M.
        ..........
        """
    ).strip()
    assert solve(task) == 9
