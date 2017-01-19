"""Day 7: Internet Protocol Version 7 tests."""

import unittest

from src.year2016.day7a import process_date, process_line, IP


class ProcessLineTest(unittest.TestCase):

    def test_basic_case(self):
        test_data = 'abba[mnop]qrst'
        expected = (
            ['abba', 'qrst'],
            ['mnop'],
        )
        self.assertEqual(process_line(test_data), expected)

    def test_long_line(self):
        test_date = 'abcd[efgh]ijkl[mnop]qrst'
        expected = (
            ['abcd', 'ijkl', 'qrst'],
            ['efgh', 'mnop'],
        )
        self.assertEqual(process_line(test_date), expected)


class PrcessDataTest(unittest.TestCase):

    def test_sample_case(self):
        test_data = 'abcd[bddb]xyyx\n' \
                    'aaaa[qwer]tyui\n'
        expected_result = [
            IP(
                main_parts=['abcd', 'xyyx'],
                hypernet_parts=['bddb']
            ),
            IP(
                main_parts=['aaaa', 'tyui'],
                hypernet_parts=['qwer'],
            )
        ]
        self.assertEqual(process_date(test_data), expected_result)
