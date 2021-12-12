"""2018 - Day 2 Part 1: Inventory Management System tests."""
from collections import Counter
from textwrap import dedent

from src.year2018.day02a import process_data
from src.year2018.day02a import solve


def test_process_data():
    expected = [Counter({"a": 2, "b": 1}), Counter({"c": 2})]
    assert list(process_data("aab\ncc")) == expected


def test_solve():
    task = dedent(
        """
        abcdef
        bababc
        abbcde
        abcccd
        aabcdd
        abcdee
        ababab
    """
    )
    assert solve(task) == 12
