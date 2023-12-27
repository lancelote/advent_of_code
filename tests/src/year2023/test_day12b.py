"""2023 - Day 12 Part 2: Hot Springs"""
from textwrap import dedent

from src.year2023.day12b import solve


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
    assert solve(task) == 525152
