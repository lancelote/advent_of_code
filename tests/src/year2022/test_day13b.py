"""2022 - Day 13 Part 2: Distress Signal."""
from textwrap import dedent

from src.year2022.day13b import solve


def test_solve():
    task = dedent(
        """
        [1,1,3,1,1]
        [1,1,5,1,1]

        [[1],[2,3,4]]
        [[1],4]

        [9]
        [[8,7,6]]

        [[4,4],4,4]
        [[4,4],4,4,4]

        [7,7,7,7]
        [7,7,7]

        []
        [3]

        [[[]]]
        [[]]

        [1,[2,[3,[4,[5,6,7]]]],8,9]
        [1,[2,[3,[4,[5,6,0]]]],8,9]
        """
    ).strip()
    assert solve(task) == 140
