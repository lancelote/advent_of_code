import pytest

from src.utils.cli import capture
from src.year2019.intcode import Computer


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

    assert computer.instruction_pointer == 0
    assert computer.opcode == 1
    assert computer.mode == ''

    computer.next()
    assert computer.instruction_pointer == 1
    assert computer.opcode == 2
    assert computer.mode == ''

    computer.next()
    assert computer.instruction_pointer == 2
    assert computer.opcode == 3
    assert computer.mode == ''


@pytest.mark.parametrize('raw_opcodes,expected_opcodes', [
    ('1,0,0,0,99', [2, 0, 0, 0, 99]),
    ('2,3,0,3,99', [2, 3, 0, 6, 99]),
    ('2,4,4,5,99,0', [2, 4, 4, 5, 99, 9801]),
    ('1,1,1,4,99,5,6,0,99', [30, 1, 1, 4, 2, 5, 6, 0, 99]),
    ('1002,4,3,4,33', [1002, 4, 3, 4, 99]),
    ('1101,100,-1,4,0', [1101, 100, -1, 4, 99]),
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
def test_input(computer, program, user_text, expected_dram):
    computer.load_program(program)

    with capture(user_text):
        computer.execute()

    assert computer.dram == expected_dram


def test_output(computer):
    computer.load_program('4,0,99')

    with capture() as out:
        computer.execute()
    assert computer.dram == [4, 0, 99]
    assert out.getvalue() == '4\n'


def test_print_output(computer):
    computer.load_program('3,0,4,0,99')

    with capture('42') as out:
        computer.execute()

    assert computer.dram == [42, 0, 4, 0, 99]
    assert out.getvalue() == 'input: 42\n'


@pytest.mark.parametrize('program,mode,opcode', [
    ('1002', '10', 2),
    ('02', '', 2),
    ('002', '', 2),
    ('099', '', 99),
])
def test_next_opcode_with_mode(program, mode, opcode, computer):
    computer.load_program(program)
    computer.load_sram_to_dram()

    assert computer.opcode == opcode
    assert computer.mode == mode
