"""2016 - Day 5 Part 2: How About a Nice Game of Chess."""

import unittest

from src.year2016.day5a import solve


class ComputeHexHash(unittest.TestCase):
    def test_compute_hex_hash(self):
        self.assertEqual(solve("abc"), "18f47a30")
