# pylint: disable=protected-access

"""Day 7: Internet Protocol Version 7 tests."""

import unittest

from src.year2016.day7a import solve, process_date, process_line, IP


class ProcessLineTest(unittest.TestCase):

    def test_basic_case(self):
        test_data = 'abba[mnop]qrst'
        expected_ip = IP(['abba', 'qrst'], ['mnop'])
        self.assertEqual(process_line(test_data), expected_ip)

    def test_long_line(self):
        test_date = 'abcd[efgh]ijkl[mnop]qrst'
        expected_ip = IP(['abcd', 'ijkl', 'qrst'], ['efgh', 'mnop'])
        self.assertEqual(process_line(test_date), expected_ip)


class ProcessDataTest(unittest.TestCase):

    def test_sample_case(self):
        test_data = 'abcd[bddb]xyyx\n' \
                    'aaaa[qwer]tyui\n'
        expected_result = [IP(['abcd', 'xyyx'], ['bddb']),
                           IP(['aaaa', 'tyui'], ['qwer'])]
        self.assertEqual(process_date(test_data), expected_result)


class IPTest(unittest.TestCase):

    def test_eq_different_type(self):
        self.assertFalse(IP(['a'], ['b']) == (['a'], ['b']))

    def test_eq_equal(self):
        self.assertTrue(IP(['a'], ['b']) == IP(['a'], ['b']))

    def test_eq_supernet_part_differs(self):
        self.assertFalse(IP(['c'], ['b']) == IP(['a'], ['b']))

    def test_eq_hypernet_part_differs(self):
        self.assertFalse(IP(['a'], ['c']) == IP(['a'], ['b']))


class SupportTLSTest(unittest.TestCase):

    def test_simple_ok(self):
        test_ip = IP(['abba', 'qrst'], ['mnop'])
        self.assertTrue(test_ip.support_tls)

    def test_simple_bad(self):
        test_ip = IP(['abcd', 'efgh'], ['ijkl'])
        self.assertFalse(test_ip.support_tls)

    def test_ABBA_inside_hypernet(self):
        test_ip = IP(['abcd', 'xyyx'], ['bddb'])
        self.assertFalse(test_ip.support_tls)

    def test_long_parts_but_ok(self):
        test_ip = IP(['ioxxoj', 'zxcvbn'], ['asdfgh'])
        self.assertTrue(test_ip.support_tls)


class HasABBATest(unittest.TestCase):

    def test_4_length_has(self):
        self.assertTrue(IP._has_abba('abba'))

    def test_4_length_all_equal(self):
        self.assertFalse(IP._has_abba('aaaa'))

    def test_4_length_has_not(self):
        self.assertFalse(IP._has_abba('abcd'))

    def test_long_start_has(self):
        self.assertTrue(IP._has_abba('abbaqwerty'))

    def test_long_middle_has(self):
        self.assertTrue(IP._has_abba('qweabbarty'))

    def test_long_has_not(self):
        self.assertFalse(IP._has_abba('qwerty'))


class SolveTest(unittest.TestCase):

    def test_solve(self):
        task = 'abba[mnop]qrst\n' \
               'abcd[bddb]xyyx\n' \
               'aaaa[qwer]tyui\n' \
               'ioxxoj[asdfgh]zxcvbn\n'
        self.assertEqual(solve(task), 2)
