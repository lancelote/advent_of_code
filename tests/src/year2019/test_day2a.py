"""2019 - Day 2 Part 1: 1202 Program Alarm."""

import pytest

from src.year2019.day2a import Program


@pytest.mark.parametrize('raw_opcodes,expected_opcodes', [
    ('1,0,0,0,99', [1, 0, 0, 0, 99]),
    ('2,3,0,3,99', [2, 3, 0, 3, 99]),
])
def test_program_from_string(raw_opcodes, expected_opcodes):
    assert Program.from_string(raw_opcodes).opcodes == expected_opcodes


def test_program_next():
    program = Program.from_string('1,2,3')
    assert program.next() == 1
    assert program.next() == 2
    assert program.next() == 3


@pytest.mark.parametrize('raw_opcodes,expected_opcodes', [
    ('1,0,0,0,99', [2, 0, 0, 0, 99]),
    ('2,3,0,3,99', [2, 3, 0, 6, 99]),
    ('2,4,4,5,99,0', [2, 4, 4, 5, 99, 9801]),
    ('1,1,1,4,99,5,6,0,99', [30, 1, 1, 4, 2, 5, 6, 0, 99]),
])
def test_execute(raw_opcodes, expected_opcodes):
    program = Program.from_string(raw_opcodes)
    program.execute()
    assert program.opcodes == expected_opcodes
