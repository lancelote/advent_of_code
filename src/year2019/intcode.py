"""Intcode computer implementation."""

from __future__ import annotations

from abc import ABC, abstractmethod
from copy import copy
from dataclasses import dataclass, field
from typing import List


class InvalidPointerException(Exception):
    """Pointer out of the available memory."""


class InstructionException(Exception):
    """Unknown opcode-instruction value."""


class UnknownModeException(Exception):
    """Unknown mode value."""


class Instruction(ABC):
    """Abstraction over general computer instruction."""

    parameters: int

    @classmethod
    @abstractmethod
    def execute(cls, computer: Computer):
        """Execute self on a given computer."""
        ...

    # ToDo: move to computer?
    @classmethod
    def get_param_addrs(cls, n: int, computer: Computer):
        """Get given parameter for instruction."""
        mode = computer.mode.rjust(cls.parameters, '0')[-n]
        addr1 = computer.instruction_pointer + n
        addr0 = computer.dram[addr1]
        if mode == '0':  # position mode
            return addr0
        elif mode == '1':  # immediate mode
            return addr1
        else:
            raise UnknownModeException(f'unknown mode {mode}')


class Sum(Instruction):
    """Save two parameters and store the result in third."""

    parameters = 3

    @classmethod
    def execute(cls, computer: Computer):
        """Execute sum instruction."""
        addr1 = cls.get_param_addrs(1, computer)
        addr2 = cls.get_param_addrs(2, computer)
        addr3 = cls.get_param_addrs(3, computer)

        # ToDo: make methods to access dram
        computer.dram[addr3] = computer.dram[addr1] + computer.dram[addr2]

        # ToDo: extract to a method
        computer.instruction_pointer += cls.parameters + 1


class Multiply(Instruction):
    """Multiply two parameters and store the result in third."""

    parameters = 3

    @classmethod
    def execute(cls, computer: Computer):
        """Execute multiply instruction."""
        addr1 = cls.get_param_addrs(1, computer)
        addr2 = cls.get_param_addrs(2, computer)
        addr3 = cls.get_param_addrs(3, computer)

        computer.dram[addr3] = computer.dram[addr1] * computer.dram[addr2]
        computer.instruction_pointer += cls.parameters + 1


class Input(Instruction):
    """Get user input and store result in a parameter."""

    parameters = 1

    @classmethod
    def execute(cls, computer: Computer):
        """Execute input instruction."""
        addr = cls.get_param_addrs(1, computer)

        computer.dram[addr] = int(input('input: '))
        computer.instruction_pointer += cls.parameters + 1


class Print(Instruction):
    """Print the parameter."""

    parameters = 1

    @classmethod
    def execute(cls, computer: Computer):
        """Execute print instruction."""
        addr = cls.get_param_addrs(1, computer)

        print(computer.dram[addr])
        computer.instruction_pointer += cls.parameters + 1


class JumpIfTrue(Instruction):
    """Jump to a given address if parameter is not 0."""

    parameters = 2

    @classmethod
    def execute(cls, computer: Computer):
        """Execute jump instruction."""
        addr1 = cls.get_param_addrs(1, computer)
        addr2 = cls.get_param_addrs(2, computer)

        if computer.dram[addr1] != 0:
            computer.instruction_pointer = computer.dram[addr2]
        else:
            computer.instruction_pointer += cls.parameters + 1


class JumpIfFalse(Instruction):
    """Jump to a given address if parameter is 0."""

    parameters = 2

    @classmethod
    def execute(cls, computer: Computer):
        """Execute jump instruction."""
        addr1 = cls.get_param_addrs(1, computer)
        addr2 = cls.get_param_addrs(2, computer)

        if computer.dram[addr1] == 0:
            computer.instruction_pointer = computer.dram[addr2]
        else:
            computer.instruction_pointer += cls.parameters + 1


class LessThan(Instruction):
    """Check if the first parameter is less than the second."""

    parameters = 3

    @classmethod
    def execute(cls, computer: Computer):
        """Execute less than instruction."""
        addr1 = cls.get_param_addrs(1, computer)
        addr2 = cls.get_param_addrs(2, computer)
        addr3 = cls.get_param_addrs(3, computer)

        if computer.dram[addr1] < computer.dram[addr2]:
            computer.dram[addr3] = 1
        else:
            computer.dram[addr3] = 0

        computer.instruction_pointer += cls.parameters + 1


class Equals(Instruction):
    """Check if next two params are equal."""

    parameters = 3

    @classmethod
    def execute(cls, computer: Computer):
        """Execute equals instruction."""
        addr1 = cls.get_param_addrs(1, computer)
        addr2 = cls.get_param_addrs(2, computer)
        addr3 = cls.get_param_addrs(3, computer)

        if computer.dram[addr1] == computer.dram[addr2]:
            computer.dram[addr3] = 1
        else:
            computer.dram[addr3] = 0

        computer.instruction_pointer += cls.parameters + 1


class Exit(Instruction):
    """Flag execution to stop."""

    parameters = 0

    @classmethod
    def execute(cls, computer: Computer):
        """Execute exit instruction."""
        computer.halt = True


INSTRUCTIONS = {
    1: Sum,
    2: Multiply,
    3: Input,
    4: Print,
    5: JumpIfTrue,
    6: JumpIfFalse,
    7: LessThan,
    8: Equals,
    99: Exit,
}


# ToDo: private out things
@dataclass
class Computer:
    """Intcode computer.

    Stores program in memory as a list of integer and the current opcode under
    execution index.
    """

    halt: bool = False
    sram: List[int] = field(default_factory=list)  # Static memory
    dram: List[int] = field(default_factory=list)  # Dynamic memory
    instruction_pointer: int = 0

    def load_program(self, string: str):
        """Load program to memory."""
        self.sram = [int(opcode) for opcode in string.split(',')]

    def next(self):
        """Get the next instruction and increment the pointer."""
        self.instruction_pointer += 1

    def execute(self):
        """Iterate over opcodes in memory executing commands unless 99 stop."""
        assert self.sram, "no program loaded."

        self.reset()
        self.load_sram_to_dram()

        while not self.halt:
            self.instruction.execute(self)

    def set_noun_and_verb(self, noun, verb):
        """Set up the given noun and verb values."""
        self.sram[1] = noun
        self.sram[2] = verb

    def reset(self):
        """Reset the computer."""
        self.instruction_pointer = 0
        self.dram = []
        self.halt = False

    def load_sram_to_dram(self):
        """Load static memory to dynamic."""
        self.dram = copy(self.sram)

    @property
    def instruction(self):
        """Get current instruction class."""
        try:
            return INSTRUCTIONS[self.opcode]
        except KeyError:
            raise InstructionException(f'unknown opcode {self.opcode}')

    @property
    def opcode(self) -> int:
        """Return current opcode under execution from DRAM."""
        try:
            value = str(self.dram[self.instruction_pointer])
            return int(value[-2:])
        except IndexError:
            raise InvalidPointerException(f'i: {self.instruction_pointer}')

    @property
    def mode(self) -> str:
        """Return current mode under execution from DRAM."""
        try:
            value = str(self.dram[self.instruction_pointer])
            return value[:-2]
        except IndexError:
            raise InvalidPointerException(f'i: {self.instruction_pointer}')

    @property
    def output(self) -> int:
        """Output is the 0 address value."""
        assert self.dram, "no output - empty dram"
        return self.dram[0]

    @property
    def noun(self) -> int:
        """Noun is the 1 address value."""
        assert self.dram, "no noun - empty dram"
        return self.dram[1]

    @property
    def verb(self) -> int:
        """Verb is the 2 address value."""
        assert self.dram, "no verb - empty dram"
        return self.dram[2]
