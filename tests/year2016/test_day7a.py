"""Day 7: Internet Protocol Version 7 tests."""

import unittest

from src.year2016.day7a import solve, process_date, process_line,\
    support_tls, IP


class ProcessLineTest(unittest.TestCase):

    def test_basic_case(self):
        test_data = 'abba[mnop]qrst'
        expected_ip = IP(
            ['abba', 'qrst'],
            ['mnop'],
        )
        self.assertEqual(process_line(test_data), expected_ip)

    def test_long_line(self):
        test_date = 'abcd[efgh]ijkl[mnop]qrst'
        expected_ip = IP(
            ['abcd', 'ijkl', 'qrst'],
            ['efgh', 'mnop'],
        )
        self.assertEqual(process_line(test_date), expected_ip)


class ProcessDataTest(unittest.TestCase):

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


class SupportTLSTest(unittest.TestCase):

    def test_simple_ok(self):
        test_ip = IP(
            ['abba', 'qrst'],
            ['mnop']
        )
        self.assertTrue(support_tls(test_ip))

    def test_simple_bad(self):
        test_ip = IP(
            ['abcd', 'efgh'],
            ['ijkl']
        )
        self.assertFalse(support_tls(test_ip))

    def test_ABBA_inside_hypernet(self):
        test_ip = IP(
            ['abcd', 'xyyx'],
            ['bddb']
        )
        self.assertFalse(support_tls(test_ip))

    def test_long_parts_but_ok(self):
        test_ip = IP(
            ['ioxxoj', 'zxcvbn'],
            ['asdfgh']
        )
        self.assertTrue(support_tls(test_ip))


class SolveTest(unittest.TestCase):

    def test_solve(self):
        task = 'abba[mnop]qrst\n' \
               'abcd[bddb]xyyx\n' \
               'aaaa[qwer]tyui\n' \
               'ioxxoj[asdfgh]zxcvbn\n'
        self.assertEqual(solve(task), 2)
