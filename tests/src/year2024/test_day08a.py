"""2024 - Day 8 Part 1: Resonant Collinearity"""

from textwrap import dedent

from src.year2024.day08a import solve


def test_solve():
    task = dedent(
        """
        ......#....#
        ...#....0...
        ....#0....#.
        ..#....0....
        ....0....#..
        .#....A.....
        ...#........
        #......#....
        ........A...
        .........A..
        ..........#.
        ..........#.
        """
    ).strip()
    assert solve(task) == 14
