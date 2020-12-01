"""2016 - Day 2 Puzzle Part 1 tests."""

import unittest

from src.year2016.day2a import solve, processed_data, Keypad


class ProcessedDataTest(unittest.TestCase):
    def test_empty_instructions(self):
        self.assertEqual(processed_data(""), [[]])

    def test_single_line(self):
        self.assertEqual(processed_data("ULL"), [["U", "L", "L"]])

    def test_multiple_lines(self):
        self.assertEqual(processed_data("UL\nRD"), [["U", "L"], ["R", "D"]])

    def test_new_trailing_line(self):
        self.assertEqual(processed_data("U\nR\n"), [["U"], ["R"]])


class KeypadTest(unittest.TestCase):
    def setUp(self):
        self.keypad = Keypad([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    def test_start_with_5(self):
        self.assertEqual(self.keypad.current_digit, "5")

    def test_move_up(self):
        self.keypad.move("U")
        self.assertEqual(self.keypad.current_digit, "2")

    def test_move_right(self):
        self.keypad.move("R")
        self.assertEqual(self.keypad.current_digit, "6")

    def test_move_down(self):
        self.keypad.move("D")
        self.assertEqual(self.keypad.current_digit, "8")

    def test_move_left(self):
        self.keypad.move("L")
        self.assertEqual(self.keypad.current_digit, "4")

    def test_block_up(self):
        self.keypad.move("U", 2)
        self.assertEqual(self.keypad.current_digit, "2")

    def test_block_right(self):
        self.keypad.move("R", 2)
        self.assertEqual(self.keypad.current_digit, "6")

    def test_block_down(self):
        self.keypad.move("D", 2)
        self.assertEqual(self.keypad.current_digit, "8")

    def test_block_left(self):
        self.keypad.move("L", 2)
        self.assertEqual(self.keypad.current_digit, "4")

    def test_can_move_up(self):
        self.assertTrue(self.keypad.can_move_up())
        self.keypad.move("U")
        self.assertFalse(self.keypad.can_move_up())

    def test_can_move_right(self):
        self.assertTrue(self.keypad.can_move_right())
        self.keypad.move("R")
        self.assertFalse(self.keypad.can_move_right())

    def test_can_move_down(self):
        self.assertTrue(self.keypad.can_move_down())
        self.keypad.move("D")
        self.assertFalse(self.keypad.can_move_down())

    def test_can_move_left(self):
        self.assertTrue(self.keypad.can_move_left())
        self.keypad.move("L")
        self.assertFalse(self.keypad.can_move_left())


class NotStandardKeypad(unittest.TestCase):
    def setUp(self):
        self.keypad = Keypad([[1], [2, 3, 4], [5]], row=1, col=0)

    def test_start_with_2(self):
        self.assertEqual(self.keypad.current_digit, "2")

    def test_can_move_up(self):
        self.assertFalse(self.keypad.can_move_up())
        self.keypad.move("R")
        self.assertTrue(self.keypad.can_move_up())

    def test_can_move_right(self):
        self.assertTrue(self.keypad.can_move_right())
        self.keypad.move("R", 2)
        self.assertFalse(self.keypad.can_move_right())

    def test_can_move_down(self):
        self.assertFalse(self.keypad.can_move_down())
        self.keypad.move("R")
        self.assertTrue(self.keypad.can_move_down())

    def test_can_move_left(self):
        self.assertFalse(self.keypad.can_move_left())
        self.keypad.move("R")
        self.assertTrue(self.keypad.can_move_left())

    def test_complete_layout(self):
        self.assertEqual(
            self.keypad.layout, [[None, 1, None], [2, 3, 4], [None, 5, None]]
        )


class SolveTest(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve("ULL\nRRDDD\nLURDL\nUUUUD"), "1985")
