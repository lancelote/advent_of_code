"""2016 - Day 7 Part 2: Internet Protocol Version 7 tests."""

import unittest

from src.year2016.day7a import IP


class AbbasTest(unittest.TestCase):
    def test_no_aba(self):
        test_ip = IP(["abc"], ["def"])
        self.assertListEqual(list(test_ip.abas), [])

    def test_all_char_the_same(self):
        test_ip = IP(["aaa"], [])
        self.assertListEqual(list(test_ip.abas), [])

    def test_multiple_abas(self):
        test_ip = IP(["aba", "bcb"], ["ded"])
        self.assertListEqual(list(test_ip.abas), ["aba", "bcb"])


class SupportSSLTest(unittest.TestCase):
    def test_aba_in_first_supernet(self):
        test_ip = IP(["aba", "xyz"], ["bab"])
        self.assertTrue(test_ip.support_ssl)

    def test_no_bab(self):
        test_ip = IP(["xyx", "xyx"], ["xyx"])
        self.assertFalse(test_ip.support_ssl)

    def test_aba_in_second_supernet(self):
        test_ip = IP(["aaa", "eke"], ["kek"])
        self.assertTrue(test_ip.support_ssl)

    def test_odd_aba_without_bab(self):
        test_ip = IP(["zazbz", "cdb"], ["bzb"])
        self.assertTrue(test_ip.support_ssl)

    def test_first_aba_has_not_bab(self):
        test_ip = IP(["aba", "cdc"], ["dcd"])
        self.assertTrue(test_ip.support_ssl)
