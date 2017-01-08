"""2016 - Day 6 Part 1: Signals and Noise tests."""

import unittest

from src.year2016.day6a import process_data, solve


class ProcessDataTest(unittest.TestCase):

    def test_process_data(self):
        data = "eedadn\ndrvtee\neandsr\n"
        expected = [
            ('e', 'd', 'e'),
            ('e', 'r', 'a'),
            ('d', 'v', 'n'),
            ('a', 't', 'd'),
            ('d', 'e', 's'),
            ('n', 'e', 'r'),
        ]
        self.assertEqual(process_data(data), expected)


class SolveTest(unittest.TestCase):

    def test_solve(self):
        task = 'eedadn\n' \
               'drvtee\n' \
               'eandsr\n' \
               'raavrd\n' \
               'atevrs\n' \
               'tsrnev\n' \
               'sdttsa\n' \
               'rasrtv\n' \
               'nssdts\n' \
               'ntnada\n' \
               'svetve\n' \
               'tesnvt\n' \
               'vntsnd\n' \
               'vrdear\n' \
               'dvrsen\n' \
               'enarar\n'
        self.assertEqual(solve(task), 'easter')
