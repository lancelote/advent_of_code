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

    @classmethod
    def get_param_addrs(cls, n: int, computer: Computer):
        """Get given parameter for instruction."""
        mode = computer.mode.rjust(cls.parameters, '0')[-n]
        addr1 = computer.current_position + n
        addr0 = computer.get(addr1)
        if mode == '0':  # position mode
            return addr0
        elif mode == '1':  # immediate mode
            return addr1
        else:
            raise UnknownModeException(f'unknown mode {mode}')

    @classmethod
    def next_instruction(cls, computer: Computer):
        """Move the instruction pointer to next instruction."""
        computer.next(cls.parameters + 1)


class Sum(Instruction):
    """Save two parameters and store the result in third."""

    parameters = 3

    @classmethod
    def execute(cls, computer: Computer):
        """Execute sum instruction."""
        addr1 = cls.get_param_addrs(1, computer)
        addr2 = cls.get_param_addrs(2, computer)
        addr3 = cls.get_param_addrs(3, computer)

        computer.set(addr3, computer.get(addr1) + computer.get(addr2))
        cls.next_instruction(computer)


class Multiply(Instruction):
    """Multiply two parameters and store the result in third."""

    parameters = 3

    @classmethod
    def execute(cls, computer: Computer):
        """Execute multiply instruction."""
        addr1 = cls.get_param_addrs(1, computer)
        addr2 = cls.get_param_addrs(2, computer)
        addr3 = cls.get_param_addrs(3, computer)

        computer.set(addr3, computer.get(addr1) * computer.get(addr2))
        cls.next_instruction(computer)


class Input(Instruction):
    """Get user input and store result in a parameter."""

    parameters = 1

    @classmethod
    def execute(cls, computer: Computer):
        """Execute input instruction."""
        addr = cls.get_param_addrs(1, computer)

        computer.set(addr, int(input()))
        cls.next_instruction(computer)


class Print(Instruction):
    """Print the parameter."""

    parameters = 1

    @classmethod
    def execute(cls, computer: Computer):
        """Execute print instruction."""
        addr = cls.get_param_addrs(1, computer)

        print(computer.get(addr))
        cls.next_instruction(computer)


class JumpIfTrue(Instruction):
    """Jump to a given address if parameter is not 0."""

    parameters = 2

    @classmethod
    def execute(cls, computer: Computer):
        """Execute jump instruction."""
        addr1 = cls.get_param_addrs(1, computer)
        addr2 = cls.get_param_addrs(2, computer)

        if computer.get(addr1) != 0:
            computer.jump(computer.get(addr2))
        else:
            cls.next_instruction(computer)


class JumpIfFalse(Instruction):
    """Jump to a given address if parameter is 0."""

    parameters = 2

    @classmethod
    def execute(cls, computer: Computer):
        """Execute jump instruction."""
        addr1 = cls.get_param_addrs(1, computer)
        addr2 = cls.get_param_addrs(2, computer)

        if computer.get(addr1) == 0:
            computer.jump(computer.get(addr2))
        else:
            cls.next_instruction(computer)


class LessThan(Instruction):
    """Check if the first parameter is less than the second."""

    parameters = 3

    @classmethod
    def execute(cls, computer: Computer):
        """Execute less than instruction."""
        addr1 = cls.get_param_addrs(1, computer)
        addr2 = cls.get_param_addrs(2, computer)
        addr3 = cls.get_param_addrs(3, computer)

        if computer.get(addr1) < computer.get(addr2):
            computer.set(addr3, 1)
        else:
            computer.set(addr3, 0)

        cls.next_instruction(computer)


class Equals(Instruction):
    """Check if next two params are equal."""

    parameters = 3

    @classmethod
    def execute(cls, computer: Computer):
        """Execute equals instruction."""
        addr1 = cls.get_param_addrs(1, computer)
        addr2 = cls.get_param_addrs(2, computer)
        addr3 = cls.get_param_addrs(3, computer)

        if computer.get(addr1) == computer.get(addr2):
            computer.set(addr3, 1)
        else:
            computer.set(addr3, 0)

        cls.next_instruction(computer)


class Exit(Instruction):
    """Flag execution to stop."""

    parameters = 0

    @classmethod
    def execute(cls, computer: Computer):
        """Execute exit instruction."""
        computer.stop()


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


@dataclass
class Computer:
    """Intcode computer.

    Stores program in memory as a list of integer and the current opcode under
    execution index.
    """

    _is_halt: bool = False
    _sram: List[int] = field(default_factory=list)  # Static memory
    _dram: List[int] = field(default_factory=list)  # Dynamic memory
    _instruction_pointer: int = 0

    def load_program(self, string: str):
        """Load program to memory."""
        self._sram = [int(opcode) for opcode in string.split(',')]

    def next(self, n: int = 1):
        """Get the next instruction and increment the pointer."""
        self._instruction_pointer += n

    def execute(self):
        """Iterate over opcodes in memory executing commands unless 99 stop."""
        assert self._sram, "no program loaded."

        self.reset()
        self.load_sram_to_dram()

        while not self._is_halt:
            self.instruction.execute(self)

    def set_noun_and_verb(self, noun, verb):
        """Set up the given noun and verb values."""
        self._sram[1] = noun
        self._sram[2] = verb

    def reset(self):
        """Reset the computer."""
        self._instruction_pointer = 0
        self._dram = []
        self._is_halt = False

    def load_sram_to_dram(self):
        """Load static memory to dynamic."""
        self._dram = copy(self._sram)

    def get(self, addr: int) -> int:
        """Get given address value."""
        return self._dram[addr]

    def set(self, addr: int, value: int):
        """Set given address value."""
        self._dram[addr] = value

    def jump(self, addr: int):
        """Move instruction pointer to a given address."""
        self._instruction_pointer = addr

    def stop(self):
        """Mark execution to stop."""
        self._is_halt = True

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
            value = str(self._dram[self._instruction_pointer])
            return int(value[-2:])
        except IndexError:
            raise InvalidPointerException(f'i: {self._instruction_pointer}')

    @property
    def mode(self) -> str:
        """Return current mode under execution from DRAM."""
        try:
            value = str(self._dram[self._instruction_pointer])
            return value[:-2]
        except IndexError:
            raise InvalidPointerException(f'i: {self._instruction_pointer}')

    @property
    def output(self) -> int:
        """Output is the 0 address value."""
        assert self._dram, "no output - empty dram"
        return self._dram[0]

    @property
    def noun(self) -> int:
        """Noun is the 1 address value."""
        assert self._dram, "no noun - empty dram"
        return self._dram[1]

    @property
    def verb(self) -> int:
        """Verb is the 2 address value."""
        assert self._dram, "no verb - empty dram"
        return self._dram[2]

    @property
    def current_position(self) -> int:
        """Return current instruction pointer address."""
        return self._instruction_pointer
