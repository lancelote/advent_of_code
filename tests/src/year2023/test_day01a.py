"""2023 - Day 1 Part 1: Trebuchet?!"""

from textwrap import dedent

import pytest

from src.year2023.day01a import get_num, solve


@pytest.mark.parametrize(
    "line,expected",
    (
        ("1abc2", 12),
        ("pqr3stu8vwx", 38),
        ("a1b2c3d4e5f", 15),
        ("treb7uchet", 77),
    ),
)
def test_get_num(line, expected):
    assert get_num(line) == expected


def test_solve():
    task = dedent(
        """
        1abc2
        pqr3stu8vwx
        a1b2c3d4e5f
        treb7uchet
        """.strip()
    )
    assert solve(task) == 142
