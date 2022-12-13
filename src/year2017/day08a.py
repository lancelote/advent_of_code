"""2017 - Day 8 Part 1: I Heard You Like Registers.

You receive a signal directly from the CPU. Because of your recent assistance
with jump instructions, it would like you to compute the result of a series of
unusual register instructions.

Each instruction consists of several parts: the register to modify, whether to
increase or decrease that register's value, the amount by which to increase or
decrease it, and a condition. If the condition fails, skip the instruction
without modifying the register. The registers all start at 0. The instructions
look like this:

    b inc 5 if a > 1
    a inc 1 if b < 5
    c dec -10 if a >= 1
    c inc -20 if c == 10

These instructions would be processed as follows:

    - Because a starts at 0, it is not greater than 1, and so b is not
      modified.
    - a is increased by 1 (to 1) because b is less than 5 (it is 0).
    - c is decreased by -10 (to 10) because a is now greater than or equal
      to 1 (it is 1).
    - c is increased by -20 (to -10) because c is equal to 10.

After this process, the largest value in any register is 1.

You might also encounter <= (less than or equal to) or != (not equal to).
However, the CPU doesn't have the bandwidth to tell you what all the registers
are named, and leaves that to you to determine.

What is the largest value in any register after completing the instructions in
your puzzle input?
"""
import operator
from collections import defaultdict
from collections import namedtuple
from typing import DefaultDict

Instruction = namedtuple(
    "Instruction", ["register", "op", "value", "base", "check", "limit"]
)

OPERATORS = {
    ">": operator.gt,
    "<": operator.lt,
    ">=": operator.ge,
    "<=": operator.le,
    "==": operator.eq,
    "!=": operator.ne,
    "inc": operator.iadd,
    "dec": operator.isub,
}


def process_line(line: str) -> Instruction:
    """Convert single line in Instruction instance."""
    register, op, value, _, base, check, limit = line.split()
    return Instruction(register, op, int(value), base, check, int(limit))


def process_data(data: str) -> list[Instruction]:
    """Convert raw data in the easy-to-use list of Instruction instances."""
    instructions = []
    for line in data.strip().split("\n"):
        instruction = process_line(line)
        instructions.append(instruction)
    return instructions


def perform_instructions(
    instructions: list[Instruction],
) -> tuple[DefaultDict[str, int], int]:
    """Apply all instructions and return registers + the biggest value seen."""
    registers: DefaultDict[str, int] = defaultdict(int)
    biggest = 0

    for instruction in instructions:
        update = OPERATORS[instruction.op]
        check = OPERATORS[instruction.check]
        register = instruction.register
        old_value = registers[register]
        base = registers[instruction.base]
        if check(base, instruction.limit):
            registers[register] = update(old_value, instruction.value)
            if registers[register] > biggest:
                biggest = registers[register]
    return registers, biggest


def solve(task: str) -> int:
    """Find the biggest register."""
    instructions = process_data(task)
    registers, _ = perform_instructions(instructions)
    return max(registers.values())
