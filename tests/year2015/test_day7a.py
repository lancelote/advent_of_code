# coding=utf-8
# pylint: disable=missing-docstring

"""
Day 7 Puzzle Part 1 tests
"""

import unittest

from src.year2015.day7a import process_data


class TestProcessData(unittest.TestCase):

    def test_return_correct_result(self):
        self.assertEqual(
            process_data('123 -> x'),
            [(None, None, '123', 'x')]
        )
        self.assertEqual(
            process_data('x AND y -> z'),
            [('x', 'AND', 'y', 'z')]
        )
        self.assertEqual(
            process_data('p LSHIFT 2 -> q'),
            [('p', 'LSHIFT', '2', 'q')]
        )
        self.assertEqual(
            process_data('NOT e -> f'),
            [(None, 'NOT', 'e', 'f')]
        )


class TestSolve(unittest.TestCase):

    def test_returns_correct_result(self):
        pass
