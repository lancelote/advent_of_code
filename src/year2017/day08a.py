"""2017 - Day 8 Part 1: I Heard You Like Registers."""

import operator
from collections import defaultdict, namedtuple
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
