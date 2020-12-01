"""2017 - Day 1 Part 2: Inverse Captcha tests."""

from src.year2017.day1b import solve


class TestSolve:
    def test_all_match(self):
        assert solve("1212") == 6
        assert solve("123123") == 12

    def test_no_match(self):
        assert solve("1221") == 0

    def test_one_match(self):
        assert solve("123425") == 4

    def test_few_match(self):
        assert solve("12131415") == 4
