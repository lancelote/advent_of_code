"""2024 - Day 4 Part 1: Ceres Search"""

from textwrap import dedent

from src.year2024.day04a import solve


def test_solve():
    task = dedent(
        """
        MMMSXXMASM
        MSAMXMSMSA
        AMXSXMAAMM
        MSAMASMSMX
        XMASAMXAMM
        XXAMMXXAMA
        SMSMSASXSS
        SAXAMASAAA
        MAMMMXMMMM
        MXMXAXMASX
        """
    ).strip()
    assert solve(task) == 18
