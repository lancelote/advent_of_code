import sys
from io import StringIO
from contextlib import contextmanager

import pytest

from src.year2019.intcode import Computer


@contextmanager
def mock_stdin(new_text: str):
    original = sys.stdin
    sys.stdin = StringIO(new_text)
    yield
    sys.stdin = original


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
    assert computer.next() == (1, '')
    assert computer.next() == (2, '')
    assert computer.next() == (3, '')


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


@pytest.mark.parametrize('program,user_text,expected_dram', [
    ('3,0,99', '7', [7, 0, 99]),
    ('3,1,99', '6', [3, 6, 99]),
])
def test_print(computer, program, user_text, expected_dram):
    computer.load_program(program)

    with mock_stdin(user_text):
        computer.execute()

    assert computer.dram == expected_dram


def test_output(computer, capsys):
    computer.load_program('4,0,99')
    computer.execute()
    assert computer.dram == [4, 0, 99]
    assert capsys.readouterr().out == '4\n'


def test_print_output(computer, capsys):
    computer.load_program('3,0,4,0,99')

    with mock_stdin('42'):
        computer.execute()

    assert computer.dram == [42, 0, 4, 0, 99]
    assert capsys.readouterr().out == '42\n'


@pytest.mark.parametrize('program,opcode,mode', [
    ('1002', 2, '10'),
    ('02', 2, ''),
    ('002', 2, ''),
    ('099', 99, ''),
])
def test_next_opcode_with_mode(program, opcode, mode, computer):
    computer.load_program(program)
    computer.load_sram_to_dram()
    assert computer.next() == (opcode, mode)
