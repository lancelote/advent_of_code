from copy import copy
from dataclasses import dataclass, field
from typing import List


class InvalidPointerException(Exception):
    """Pointer out of the available memory."""


class OpcodeException(Exception):
    """Unknown opcode value."""


@dataclass
class Computer:
    """Intcode computer.

    Stores program in memory as a list of integer and the current opcode under
    execution index.
    """

    sram: List[int] = field(default_factory=list)  # Static memory
    dram: List[int] = field(default_factory=list)  # Dynamic memory
    instruction_pointer: int = 0

    def load_program(self, string: str):
        """Load program to memory."""
        self.sram = [int(opcode) for opcode in string.split(',')]

    def next(self):
        """Get the next instruction and increment the pointer."""
        try:
            value = str(self.dram[self.instruction_pointer])
            opcode = int(value[-2:])
            mode = value[:-2]
            self.instruction_pointer += 1
            return opcode, mode
        except IndexError:
            raise InvalidPointerException(f'i: {self.instruction_pointer}')

    def execute(self):
        """Iterate over opcodes in memory executing commands unless 99 stop."""
        assert self.sram, "no program loaded."

        self.reset()
        self.load_sram_to_dram()

        while True:
            opcode, mode = self.next()
            if opcode == 1:
                self.sum()
            elif opcode == 2:
                self.multiply()
            elif opcode == 3:
                self.input()
            elif opcode == 4:
                self.print()
            elif opcode == 99:
                break
            else:
                raise OpcodeException(f'unknown opcode: {opcode}')

    def sum(self):
        """Sum next 2 opcodes and store the result in 3."""
        address1 = self.instruction_pointer
        address2 = self.instruction_pointer + 1
        address3 = self.instruction_pointer + 2

        param1 = self.dram[address1]
        param2 = self.dram[address2]
        param3 = self.dram[address3]

        self.dram[param3] = self.dram[param1] + self.dram[param2]
        self.instruction_pointer += 3

    def multiply(self):
        """Multiply next 2 opcodes and store the result in 3."""
        address1 = self.instruction_pointer
        address2 = self.instruction_pointer + 1
        address3 = self.instruction_pointer + 2

        param1 = self.dram[address1]
        param2 = self.dram[address2]
        param3 = self.dram[address3]

        self.dram[param3] = self.dram[param1] * self.dram[param2]
        self.instruction_pointer += 3

    def input(self):
        address = self.instruction_pointer
        param = self.dram[address]
        self.dram[param] = int(input())
        self.instruction_pointer += 1

    def print(self):
        address = self.instruction_pointer
        param = self.dram[address]
        print(self.dram[param])
        self.instruction_pointer += 1

    def set_noun_and_verb(self, noun, verb):
        """Set up the given noun and verb values."""
        self.sram[1] = noun
        self.sram[2] = verb

    def reset(self):
        """Reset the computer."""
        self.instruction_pointer = 0
        self.dram = []

    def load_sram_to_dram(self):
        """Load static memory to dynamic."""
        self.dram = copy(self.sram)

    @property
    def output(self):
        """Output is the 0 address value."""
        assert self.dram, "no output - empty dram"
        return self.dram[0]

    @property
    def noun(self):
        """Noun is the 1 address value."""
        assert self.dram, "no noun - empty dram"
        return self.dram[1]

    @property
    def verb(self):
        """Verb is the 2 address value."""
        assert self.dram, "no verb - empty dram"
        return self.dram[2]
