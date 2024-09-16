"""2023 - Day 11 Part 2: Cosmic Expansion"""

from textwrap import dedent

import pytest

from src.year2023.day11b import StarMap


@pytest.mark.parametrize(
    "age,expected",
    (
        (2, 374),  # default
        (10, 1030),
        (100, 8410),
    ),
)
def test_star_map(age, expected):
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
        ).strip(),
        age,
    )

    assert sm.total_path == expected
