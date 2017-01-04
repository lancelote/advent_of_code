"""2016 - Day 4 Puzzle Part 1 tests."""

import unittest

from src.year2016.day4a import solve, process_data, is_real, Room


class ProcessDataTest(unittest.TestCase):

    def test_process_data(self):
        task = 'aaaaa-bbb-z-y-x-123[abxyz]\na-b-c-d-e-f-g-h-987[abcde]'
        rooms = [
            Room('aaaaabbbzyx', 123, 'abxyz'),
            Room('abcdefgh', 987, 'abcde'),
        ]
        self.assertEqual(process_data(task), rooms)


class IsRealTest(unittest.TestCase):

    def test_all_sorted(self):
        self.assertTrue(is_real(Room('aaaaabbbzyx', 123, 'abxyz')))

    def test_all_once(self):
        self.assertTrue(is_real(Room('abcdefgh', 987, 'abcde')))

    def test_real_mix(self):
        self.assertTrue(is_real(Room('notarealroom', 404, 'oarel')))

    def test_not_real_mix(self):
        self.assertFalse(is_real(Room('totallyrealroom', 200, 'decoy')))


class SolveTest(unittest.TestCase):

    def test_solve(self):
        task = 'aaaaa-bbb-z-y-x-123[abxyz]\n' \
               'a-b-c-d-e-f-g-h-987[abcde]\n' \
               'not-a-real-room-404[oarel]\n' \
               'totally-real-room-200[decoy]\n'
        self.assertEqual(solve(task), 1514)
