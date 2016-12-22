# pylint: disable=missing-docstring, invalid-name

"""2016 - Day 2 Puzzle Part 1 tests."""

import unittest

from src.year2016.day2a import solve, processed_data, Keypad


class ProcessedDataTest(unittest.TestCase):

    def test_empty_instructions(self):
        self.assertEqual(processed_data(''), [[]])

    def test_single_line(self):
        self.assertEqual(processed_data('ULL'), [['U', 'L', 'L']])

    def test_multiple_lines(self):
        self.assertEqual(processed_data('UL\nRD'), [['U', 'L'], ['R', 'D']])


class KeypadTest(unittest.TestCase):

    def test_de_init(self):
        keypad =


class SolveTest(unittest.TestCase):

    @unittest.skip
    def test_solve(self):
        self.assertEqual(solve('ULL\nRRDDD\nLURDL\nUUUUD'), 1985)
