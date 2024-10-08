"""2018 - Day 2 Part 2: Inventory Management System tests."""

from textwrap import dedent

from src.year2018.day02b import get_similar_id_part
from src.year2018.day02b import solve


def test_get_similar_id_part():
    assert get_similar_id_part("aabc", "abba") == "ab"


def test_solve():
    task = dedent(
        """
        abcde
        fghij
        klmno
        pqrst
        fguij
        axcye
        wvxyz
    """
    )
    assert solve(task) == "fgij"
