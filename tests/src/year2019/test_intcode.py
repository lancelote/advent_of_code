from src.year2019.intcode import Computer

import pytest


@pytest.fixture
def computer():
    return Computer()


@pytest.mark.parametrize('raw_opcodes,expected_opcodes', [
    ('1,0,0,0,99', [1, 0, 0, 0, 99]),
    ('2,3,0,3,99', [2, 3, 0, 3, 99]),
])
def test_program_from_string(computer, raw_opcodes, expected_opcodes):
    computer.load_program(raw_opcodes)
    assert computer.sram == expected_opcodes


def test_program_next(computer):
    computer.load_program('1,2,3')
    computer.load_sram_to_dram()
    assert computer.next() == 1
    assert computer.next() == 2
    assert computer.next() == 3


@pytest.mark.parametrize('raw_opcodes,expected_opcodes', [
    ('1,0,0,0,99', [2, 0, 0, 0, 99]),
    ('2,3,0,3,99', [2, 3, 0, 6, 99]),
    ('2,4,4,5,99,0', [2, 4, 4, 5, 99, 9801]),
    ('1,1,1,4,99,5,6,0,99', [30, 1, 1, 4, 2, 5, 6, 0, 99]),
])
def test_execute(computer, raw_opcodes, expected_opcodes):
    computer.load_program(raw_opcodes)
    computer.execute()
    assert computer.dram == expected_opcodes


def test_set_noun_and_verb(computer):
    computer.load_program('1,0,0')
    computer.set_noun_and_verb(2, 3)
    assert computer.sram[1] == 2
    assert computer.sram[2] == 3


def test_multiple_executions(computer):
    computer.load_program('1,0,0,0,99')
    computer.execute()

    assert computer.instruction_pointer == 5
    assert computer.sram[0] == 1
    assert computer.dram[0] == 2

    computer.execute()

    assert computer.instruction_pointer == 5
    assert computer.sram[0] == 1
    assert computer.dram[0] == 2
