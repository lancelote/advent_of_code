"""2016 - Day 4 Puzzle Part 2 tests."""

import unittest

from src.year2016.day04b import decipher
from src.year2016.day04b import shift
from src.year2016.day04b import solve


class ShiftTest(unittest.TestCase):
    def test_simple_case(self):
        self.assertEqual(shift("a", 1), "b")

    def test_last_char(self):
        self.assertEqual(shift("z", 1), "a")

    def test_long_shift(self):
        self.assertEqual(shift("a", 3), "d")

    def test_one_new_cycle(self):
        self.assertEqual(shift("y", 3), "b")

    def test_full_cycle(self):
        self.assertEqual(shift("a", 26), "a")

    def test_two_full_cycles(self):
        self.assertEqual(shift("a", 52), "a")

    def test_multiple_cycles(self):
        self.assertEqual(shift("b", 53), "c")

    def test_space(self):
        self.assertEqual(shift("-", 123), " ")


class DecipherTest(unittest.TestCase):
    def test_decipher(self):
        ciphered_name = "qzmt-zixmtkozy-ivhz"
        deciphered_name = "very encrypted name"
        self.assertEqual(decipher(ciphered_name, 343), deciphered_name)


class SolveTest(unittest.TestCase):
    def test_solve(self):
        task = "ijmockjgz-jwezxo-nojmvbz-993[jozmb]"
        self.assertEqual(solve(task), 993)
