"""2017 - Day 2 Part 2: Corruption Checksum tests."""
from src.year2017.day2b import find_division
from src.year2017.day2b import solve


class TestFindDivision:
    def test_small_first(self):
        assert find_division([5, 9, 2, 8]) == 4
        assert find_division([3, 8, 6, 5]) == 2

    def test_small_last(self):
        assert find_division([9, 4, 7, 3]) == 3

    def test_no_division(self):
        assert find_division([2, 3, 5, 7]) == 0

    def test_multiple_division(self):
        assert find_division([2, 4, 3, 6]) == 2


def test_solve():
    data = """5	9	2	8
    9	4	7	3
    3	8	6	5"""
    assert solve(data) == 9
