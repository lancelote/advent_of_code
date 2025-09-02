"""2023 - Day 12 Part 1: Hot Springs"""

from textwrap import dedent

import pytest

from src.year2023.day12a import Row
from src.year2023.day12a import solve


@pytest.mark.parametrize(
    "line,expected",
    (
        ("???.### 1,1,3", 1),
        (".??..??...?##. 1,1,3", 4),
        ("?#?#?#?#?#?#?#? 1,3,1,6", 1),
        ("????.#...#... 4,1,1", 1),
        ("????.######..#####. 1,6,5", 4),
        ("?###???????? 3,2,1", 10),
    ),
)
def test_row(line, expected):
    assert Row.from_line(line).arrangements == expected


def test_solve():
    task = dedent(
        """
        ???.### 1,1,3
        .??..??...?##. 1,1,3
        ?#?#?#?#?#?#?#? 1,3,1,6
        ????.#...#... 4,1,1
        ????.######..#####. 1,6,5
        ?###???????? 3,2,1
        """
    ).strip()
    assert solve(task) == 21
