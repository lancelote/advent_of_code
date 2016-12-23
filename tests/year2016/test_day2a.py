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

    def test_new_trailing_line(self):
        self.assertEqual(processed_data('U\nR\n'), [['U'], ['R']])


class KeypadTest(unittest.TestCase):

    def setUp(self):
        self.keypad = Keypad()

    def test_start_with_5(self):
        self.assertEqual(self.keypad.current_digit(), '5')

    def test_move_up(self):
        self.keypad.move('U')
        self.assertEqual(self.keypad.current_digit(), '2')

    def test_move_right(self):
        self.keypad.move('R')
        self.assertEqual(self.keypad.current_digit(), '6')

    def test_move_down(self):
        self.keypad.move('D')
        self.assertEqual(self.keypad.current_digit(), '8')

    def test_move_left(self):
        self.keypad.move('L')
        self.assertEqual(self.keypad.current_digit(), '4')

    def test_block_up(self):
        self.keypad.move('U', 2)
        self.assertEqual(self.keypad.current_digit(), '2')

    def test_block_right(self):
        self.keypad.move('R', 2)
        self.assertEqual(self.keypad.current_digit(), '6')

    def test_block_down(self):
        self.keypad.move('D', 2)
        self.assertEqual(self.keypad.current_digit(), '8')

    def test_block_left(self):
        self.keypad.move('L', 2)
        self.assertEqual(self.keypad.current_digit(), '4')

    def test_unknown_instruction(self):
        with self.assertRaises(ValueError):
            self.keypad.move('A')


class SolveTest(unittest.TestCase):

    def test_solve(self):
        self.assertEqual(solve('ULL\nRRDDD\nLURDL\nUUUUD'), 1985)
