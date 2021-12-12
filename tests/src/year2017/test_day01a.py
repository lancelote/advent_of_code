"""2017 - Day 1 Part 1: Inverse Captcha tests."""
from src.year2017.day01a import solve


class TestSolve:
    def test_two_digits_match(self):
        assert solve("11") == 2

    def test_two_different_digits_match(self):
        assert solve("1122") == 3

    def test_all_digits_match(self):
        assert solve("1111") == 4

    def test_no_digits_match(self):
        assert solve("1234") == 0

    def test_only_last_digit_match(self):
        assert solve("91212129") == 9
