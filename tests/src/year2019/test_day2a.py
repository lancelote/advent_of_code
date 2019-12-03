"""2019 - Day 2 Part 1: 1202 Program Alarm."""

import pytest

from src.year2019.day2a import Intcode


@pytest.mark.parametrize('raw_opcodes,expected_opcodes', [
    ('1,0,0,0,99', [1, 0, 0, 0, 99]),
    ('2,3,0,3,99', [2, 3, 0, 3, 99]),
])
def test_intcode_from_string(raw_opcodes, expected_opcodes):
    assert Intcode.from_string(raw_opcodes).opcodes == expected_opcodes
