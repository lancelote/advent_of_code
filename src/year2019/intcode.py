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


class Instruction(ABC):
    """Abstraction over general computer instruction."""

    @property
    @abstractmethod
    def parameters(self):
        """Return number of parameters instruction has."""
        ...

    @staticmethod
    @abstractmethod
    def execute(computer: Computer):
        """Execute self on a given computer."""
        ...


class Sum(Instruction):
    """Save two parameters and store the result in third."""

    parameters = 3

    @staticmethod
    def execute(computer: Computer):
        """Execute sum instruction."""
        address1 = computer.instruction_pointer + 1
        address2 = computer.instruction_pointer + 2
        address3 = computer.instruction_pointer + 3

        param1 = computer.dram[address1]
        param2 = computer.dram[address2]
        param3 = computer.dram[address3]

        computer.dram[param3] = computer.dram[param1] + computer.dram[param2]
        computer.instruction_pointer += 3


class Multiply(Instruction):
    """Multiply two parameters and store the result in third."""

    parameters = 3

    @staticmethod
    def execute(computer: Computer):
        """Execute multiply instruction."""
        address1 = computer.instruction_pointer + 1
        address2 = computer.instruction_pointer + 2
        address3 = computer.instruction_pointer + 3

        param1 = computer.dram[address1]
        param2 = computer.dram[address2]
        param3 = computer.dram[address3]

        computer.dram[param3] = computer.dram[param1] * computer.dram[param2]
        computer.instruction_pointer += 3


class Input(Instruction):
    """Get user input and store result in a parameter."""

    parameters = 1

    @staticmethod
    def execute(computer: Computer):
        """Execute input instruction."""
        address = computer.instruction_pointer + 1

        param = computer.dram[address]

        computer.dram[param] = int(input())
        computer.instruction_pointer += 1


class Print(Instruction):
    """Print the parameter."""

    parameters = 1

    @staticmethod
    def execute(computer: Computer):
        """Execute print instruction."""
        address = computer.instruction_pointer + 1

        param = computer.dram[address]

        print(computer.dram[param])
        computer.instruction_pointer += 1


class Exit(Instruction):
    """Flag execution to stop."""

    parameters = 0

    @staticmethod
    def execute(computer: Computer):
        """Execute exit instruction."""
        computer.halt = True


INSTRUCTIONS = {
    1: Sum,
    2: Multiply,
    3: Input,
    4: Print,
    99: Exit
}


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
            self.next()

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
