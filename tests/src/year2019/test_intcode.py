import pytest

from src.year2019.intcode import Computer


class Commands:
    """Long commands for testing."""

    JUMP_COMPARE_WITH_8 = (
        '3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,'
        '0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,'
        '20,1105,1,46,98,99'
    )
    IMMEDIATE_JUMP_EQUAL_0 = '3,3,1105,-1,9,1101,0,0,12,4,12,99,1'
    POSITION_JUMP_EQUAL_0 = '3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9'
    IMMEDIATE_LESS_THAN_8 = '3,3,1107,-1,8,3,4,3,99'
    IMMEDIATE_EQUAL_8 = '3,3,1108,-1,8,3,4,3,99'
    POSITION_LESS_THAN_8 = '3,9,7,9,10,9,4,9,99,-1,8'
    POSITION_EQUAL_8 = '3,9,8,9,10,9,4,9,99,-1,8'


@pytest.fixture
def computer():
    return Computer()


@pytest.mark.parametrize('raw_opcodes,expected_opcodes', [
    ('1,0,0,0,99', {0: 1, 1: 0, 2: 0, 3: 0, 4: 99}),
    ('2,3,0,3,99', {0: 2, 1: 3, 2: 0, 3: 3, 4: 99}),
])
def test_program_from_string(computer, raw_opcodes, expected_opcodes):
    computer.load_program(raw_opcodes)
    assert computer._sram == expected_opcodes


def test_program_next(computer):
    computer.load_program('1,2,3')
    computer.load_sram_to_dram()

    assert computer._instruction_pointer == 0
    assert computer.opcode == 1
    assert computer.mode == ''

    computer.next()
    assert computer._instruction_pointer == 1
    assert computer.opcode == 2
    assert computer.mode == ''

    computer.next()
    assert computer._instruction_pointer == 2
    assert computer.opcode == 3
    assert computer.mode == ''


@pytest.mark.parametrize('raw_opcodes,expected_opcodes', [
    (
        '1,0,0,0,99',
        {0: 2, 1: 0, 2: 0, 3: 0, 4: 99}
    ),
    (
        '2,3,0,3,99',
        {0: 2, 1: 3, 2: 0, 3: 6, 4: 99}
    ),
    (
        '2,4,4,5,99,0',
        {0: 2, 1: 4, 2: 4, 3: 5, 4: 99, 5: 9801}
    ),
    (
        '1,1,1,4,99,5,6,0,99',
        {0: 30, 1: 1, 2: 1, 3: 4, 4: 2, 5: 5, 6: 6, 7: 0, 8: 99}
    ),
    (
        '1002,4,3,4,33',
        {0: 1002, 1: 4, 2: 3, 3: 4, 4: 99}
    ),
    (
        '1101,100,-1,4,0',
        {0: 1101, 1: 100, 2: -1, 3: 4, 4: 99}
    ),
])
def test_execute(computer, raw_opcodes, expected_opcodes):
    computer.load_program(raw_opcodes)
    computer.execute()
    assert computer._dram == expected_opcodes


def test_set_noun_and_verb(computer):
    computer.load_program('1,0,0')
    computer.set_noun_and_verb(2, 3)
    assert computer._sram[1] == 2
    assert computer._sram[2] == 3


def test_multiple_executions(computer):
    computer.load_program('1,0,0,0,99')
    computer.execute()

    assert computer._instruction_pointer == 4
    assert computer._sram[0] == 1
    assert computer._dram[0] == 2

    computer.execute()

    assert computer._instruction_pointer == 4
    assert computer._sram[0] == 1
    assert computer._dram[0] == 2


@pytest.mark.parametrize('program,user_text,expected_dram', [
    ('3,0,99', 7, {0: 7, 1: 0, 2: 99}),
    ('3,1,99', 6, {0: 3, 1: 6, 2: 99}),
])
def test_input(computer, program, user_text, expected_dram):
    computer.load_program(program)
    computer.stdin.append(user_text)

    computer.execute()

    assert computer._dram == expected_dram


def test_output(computer):
    computer.load_program('4,0,99')

    computer.execute()

    assert computer._dram == {0: 4, 1: 0, 2: 99}
    assert len(computer.stdout) == 1
    assert computer.stdout.popleft() == 4


def test_print_output(computer):
    computer.load_program('3,0,4,0,99')
    computer.stdin.append(42)

    computer.execute()

    assert computer._dram == {0: 42, 1: 0, 2: 4, 3: 0, 4: 99}
    assert computer.stdout.popleft() == 42


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


@pytest.mark.parametrize('stdin,expect_stdout,command', [
    (7, 0, Commands.POSITION_EQUAL_8),
    (8, 1, Commands.POSITION_EQUAL_8),
    (9, 0, Commands.POSITION_EQUAL_8),
    (7, 1, Commands.POSITION_LESS_THAN_8),
    (8, 0, Commands.POSITION_LESS_THAN_8),
    (9, 0, Commands.POSITION_LESS_THAN_8),
    (7, 0, Commands.IMMEDIATE_EQUAL_8),
    (8, 1, Commands.IMMEDIATE_EQUAL_8),
    (9, 0, Commands.IMMEDIATE_EQUAL_8),
    (7, 1, Commands.IMMEDIATE_LESS_THAN_8),
    (8, 0, Commands.IMMEDIATE_LESS_THAN_8),
    (9, 0, Commands.IMMEDIATE_LESS_THAN_8),
    (0, 0, Commands.POSITION_JUMP_EQUAL_0),
    (2, 1, Commands.POSITION_JUMP_EQUAL_0),
    (0, 0, Commands.IMMEDIATE_JUMP_EQUAL_0),
    (3, 1, Commands.IMMEDIATE_JUMP_EQUAL_0),
    (7, 999, Commands.JUMP_COMPARE_WITH_8),
    (8, 1000, Commands.JUMP_COMPARE_WITH_8),
    (9, 1001, Commands.JUMP_COMPARE_WITH_8),
])
def test_input_compare_print(stdin, expect_stdout, command, computer):
    computer.load_program(command)
    computer.stdin.append(stdin)

    computer.execute()

    assert computer.stdout.popleft() == expect_stdout


def test_input_pause(computer):
    assert not computer.is_paused

    computer.load_program('3,1,99')
    computer.execute()

    assert computer.is_paused

    computer.stdin.append(42)
    computer.execute()

    assert not computer.is_paused
    assert computer.is_halt
    assert computer._dram == {0: 3, 1: 42, 2: 99}


def test_relative_base(computer):
    computer.offset_relative_base(2000)

    assert computer.relative_base == 2000

    computer.load_program('109,19,99')
    computer.execute()

    assert computer.relative_base == 2019


def test_output_large_number(computer):
    computer.load_program('104,1125899906842624,99')
    computer.execute()

    assert computer.stdout.pop() == 1125899906842624


def test_output_16_digit_number(computer):
    computer.load_program('1102,34915192,34915192,7,4,7,99,0')
    computer.execute()

    assert computer.stdout.pop() == 1219070632396864


def test_produce_copy_of_itself(computer):
    program = '109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99'
    computer.load_program(program)
    computer.execute()

    assert list(computer.stdout) == list(map(int, program.split(',')))
