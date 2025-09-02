"""2023 - Day 11 Part 1: Cosmic Expansion"""

from textwrap import dedent

from src.year2023.day11a import StarMap
from src.year2023.day11a import solve


def test_star_map():
    sm = StarMap.from_text(
        dedent(
            """
        ...#......
        .......#..
        #.........
        ..........
        ......#...
        .#........
        .........#
        ..........
        .......#..
        #...#.....
        """
        ).strip()
    )

    assert sm.get_path((5, 1), (9, 4)) == 9
    assert sm.get_path((0, 3), (8, 7)) == 15
    assert sm.get_path((0, 2), (6, 9)) == 17
    assert sm.get_path((9, 0), (9, 4)) == 5
    assert sm.get_path((4, 6), (9, 0)) == 14


def test_solve():
    task = dedent(
        """
        ...#......
        .......#..
        #.........
        ..........
        ......#...
        .#........
        .........#
        ..........
        .......#..
        #...#.....
        """
    ).strip()
    assert solve(task) == 374
