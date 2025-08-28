"""2023 - Day 1 Part 2: Trebuchet?!"""

from textwrap import dedent

import pytest

from src.year2023.day01b import get_num, solve


@pytest.mark.parametrize(
    "line,expected",
    (
        ("two1nine", 29),
        ("eightwothree", 83),
        ("abcone2threexyz", 13),
        ("xtwone3four", 24),
        ("4nineeightseven2", 42),
        ("zoneight234", 14),
        ("7pqrstsixteen", 76),
        ("one", 11),
        ("22", 22),
        ("one2", 12),
        ("1two", 12),
        ("onetwothree", 13),
        ("sevenine", 79),
        ("6oneightsr", 68),
    ),
)
def test_get_num(line, expected):
    assert get_num(line) == expected


def test_solve():
    task = dedent(
        """
        two1nine
        eightwothree
        abcone2threexyz
        xtwone3four
        4nineeightseven2
        zoneight234
        7pqrstsixteen
        """.strip()
    )
    assert solve(task) == 281
