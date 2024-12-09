"""2024 - Day 9 Part 2: Disk Fragmenter"""

from textwrap import dedent

from src.year2024.day09b import solve


def test_solve():
    task = dedent(
        """
        2333133121414131402
        """
    ).strip()
    assert solve(task) == 2858
