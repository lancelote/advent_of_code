"""Intcode computer implementation."""
from __future__ import annotations

from abc import ABC
from abc import abstractmethod
from collections import defaultdict
from collections import deque
from copy import copy
from dataclasses import dataclass
from dataclasses import field
from typing import DefaultDict
from typing import Deque

Memory = DefaultDict[int, int]


class InstructionException(Exception):
    """Unknown opcode-instruction value."""


class UnknownModeException(Exception):
    """Unknown mode value."""


class Instruction(ABC):
    """Abstraction over general computer instruction."""

    parameters: int

    @classmethod
    @abstractmethod
    def execute(cls, computer: Computer) -> None:
        """Execute self on a given computer."""
        ...

    @classmethod
    def get_param_addrs(cls, n: int, computer: Computer) -> int:
        """Get given parameter for instruction."""
        mode = computer.mode.rjust(cls.parameters, "0")[-n]
        addr1 = computer.current_position + n
        addr0 = computer[addr1]
        if mode == "0":  # position mode
            return addr0
        elif mode == "1":  # immediate mode
            return addr1
        elif mode == "2":  # relative mode
            return addr0 + computer.relative_base
        else:
            raise UnknownModeException(f"unknown mode {mode}")

    @classmethod
    def next_instruction(cls, computer: Computer) -> None:
        """Move the instruction pointer to next instruction."""
        computer.next(cls.parameters + 1)


class Sum(Instruction):
    """Save two parameters and store the result in third."""

    parameters = 3

    @classmethod
    def execute(cls, computer: Computer) -> None:
        """Execute sum instruction."""
        addr1 = cls.get_param_addrs(1, computer)
        addr2 = cls.get_param_addrs(2, computer)
        addr3 = cls.get_param_addrs(3, computer)

        computer[addr3] = computer[addr1] + computer[addr2]
        cls.next_instruction(computer)


class Multiply(Instruction):
    """Multiply two parameters and store the result in third."""

    parameters = 3

    @classmethod
    def execute(cls, computer: Computer) -> None:
        """Execute multiply instruction."""
        addr1 = cls.get_param_addrs(1, computer)
        addr2 = cls.get_param_addrs(2, computer)
        addr3 = cls.get_param_addrs(3, computer)

        computer[addr3] = computer[addr1] * computer[addr2]
        cls.next_instruction(computer)


class Input(Instruction):
    """Get user input and store result in a parameter."""

    parameters = 1

    @classmethod
    def execute(cls, computer: Computer) -> None:
        """Execute input instruction."""
        addr = cls.get_param_addrs(1, computer)

        try:
            computer[addr] = computer.stdin.popleft()
            cls.next_instruction(computer)
        except IndexError:
            # No input available
            computer.pause()


class Print(Instruction):
    """Print the parameter."""

    parameters = 1

    @classmethod
    def execute(cls, computer: Computer) -> None:
        """Execute print instruction."""
        addr = cls.get_param_addrs(1, computer)

        computer.stdout.append(computer[addr])
        cls.next_instruction(computer)


class JumpIfTrue(Instruction):
    """Jump to a given address if parameter is not 0."""

    parameters = 2

    @classmethod
    def execute(cls, computer: Computer) -> None:
        """Execute jump instruction."""
        addr1 = cls.get_param_addrs(1, computer)
        addr2 = cls.get_param_addrs(2, computer)

        if computer[addr1] != 0:
            computer.jump(computer[addr2])
        else:
            cls.next_instruction(computer)


class JumpIfFalse(Instruction):
    """Jump to a given address if parameter is 0."""

    parameters = 2

    @classmethod
    def execute(cls, computer: Computer) -> None:
        """Execute jump instruction."""
        addr1 = cls.get_param_addrs(1, computer)
        addr2 = cls.get_param_addrs(2, computer)

        if computer[addr1] == 0:
            computer.jump(computer[addr2])
        else:
            cls.next_instruction(computer)


class LessThan(Instruction):
    """Check if the first parameter is less than the second."""

    parameters = 3

    @classmethod
    def execute(cls, computer: Computer) -> None:
        """Execute less than instruction."""
        addr1 = cls.get_param_addrs(1, computer)
        addr2 = cls.get_param_addrs(2, computer)
        addr3 = cls.get_param_addrs(3, computer)

        if computer[addr1] < computer[addr2]:
            computer[addr3] = 1
        else:
            computer[addr3] = 0

        cls.next_instruction(computer)


class Equals(Instruction):
    """Check if next two params are equal."""

    parameters = 3

    @classmethod
    def execute(cls, computer: Computer) -> None:
        """Execute equals instruction."""
        addr1 = cls.get_param_addrs(1, computer)
        addr2 = cls.get_param_addrs(2, computer)
        addr3 = cls.get_param_addrs(3, computer)

        if computer[addr1] == computer[addr2]:
            computer[addr3] = 1
        else:
            computer[addr3] = 0

        cls.next_instruction(computer)


class RelativeBaseOffset(Instruction):
    """Change the relative base value."""

    parameters = 1

    @classmethod
    def execute(cls, computer: Computer) -> None:
        """Execute relative base offset instruction."""
        addr = cls.get_param_addrs(1, computer)

        computer.offset_relative_base(computer[addr])
        cls.next_instruction(computer)


class Exit(Instruction):
    """Flag execution to stop."""

    parameters = 0

    @classmethod
    def execute(cls, computer: Computer) -> None:
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
    9: RelativeBaseOffset,
    99: Exit,
}


@dataclass
class Computer:
    """Intcode computer.

    Stores program in memory as a list of integer and the current opcode under
    execution index.
    """

    stdin: Deque[int] = field(default_factory=deque)
    stdout: Deque[int] = field(default_factory=deque)

    is_paused: bool = False
    is_halt: bool = False

    _sram: Memory = field(default_factory=lambda: defaultdict(int))  # static
    _dram: Memory = field(default_factory=lambda: defaultdict(int))  # dynamic
    _instruction_pointer: int = 0
    _relative_base: int = 0

    def __getitem__(self, addr: int) -> int:
        assert addr >= 0
        return self._dram[addr]

    def __setitem__(self, addr: int, value: int) -> None:
        self._dram[addr] = value

    def load_program(self, string: str) -> None:
        """Load program to memory."""
        for i, opcode in enumerate(map(int, string.split(","))):
            self._sram[i] = opcode

    def next(self, n: int = 1) -> None:
        """Get the next instruction and increment the pointer."""
        self._instruction_pointer += n

    def execute(self) -> None:
        """Iterate over opcodes in memory executing commands unless 99 stop."""
        assert self.program_is_loaded, "no program loaded"

        self.is_paused = False
        if not self._dram:
            self.load_sram_to_dram()

        while not self.is_halt and not self.is_paused:
            self.instruction.execute(self)

    def set_noun_and_verb(self, noun: int, verb: int) -> None:
        """Set up the given noun and verb values."""
        self._sram[1] = noun
        self._sram[2] = verb

    def reset(self) -> None:
        """Reset the computer."""
        self._instruction_pointer = 0
        self.is_halt = False
        self.is_paused = False

    def load_sram_to_dram(self) -> None:
        """Load static memory to dynamic."""
        self._dram = copy(self._sram)

    def jump(self, addr: int) -> None:
        """Move instruction pointer to a given address."""
        self._instruction_pointer = addr

    def stop(self) -> None:
        """Mark execution to stop."""
        self.is_halt = True

    def pause(self) -> None:
        """Pause execution, e.g. to wait for stdin."""
        self.is_paused = True

    def offset_relative_base(self, value: int) -> None:
        """Add the given value to relative base."""
        self._relative_base += value

    @property
    def program_is_loaded(self) -> dict[int, int]:
        """Check if the program is loaded into the static memory."""
        return self._sram

    @property
    def instruction(self) -> type[Instruction]:
        """Get current instruction class."""
        try:
            return INSTRUCTIONS[self.opcode]
        except KeyError as exc:
            raise InstructionException(
                f"unknown opcode {self.opcode}"
            ) from exc

    @property
    def opcode(self) -> int:
        """Return current opcode under execution from DRAM."""
        value = str(self._dram[self._instruction_pointer])
        return int(value[-2:])

    @property
    def mode(self) -> str:
        """Return current mode under execution from DRAM."""
        value = str(self._dram[self._instruction_pointer])
        return value[:-2]

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

    @property
    def relative_base(self) -> int:
        """Return computer relative base."""
        return self._relative_base
