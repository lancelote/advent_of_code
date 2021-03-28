"""2020 - Day 14 Part 1: Docking Data."""
from __future__ import annotations

import re
from abc import ABC
from abc import abstractmethod
from collections import defaultdict
from dataclasses import dataclass
from typing import DefaultDict
from typing import List


class Mask:
    def __init__(self):
        self._mask = "X" * 36

    def set(self, mask: str) -> None:
        self._mask = mask

    def apply(self, value: int) -> int:
        str_value = bin(value)[2:].rjust(36, "0")
        result = []

        for bit, mask_bit in zip(str_value, self._mask):
            if mask_bit == "X":
                result.append(bit)
            elif mask_bit == "0":
                result.append("0")
            elif mask_bit == "1":
                result.append("1")
            else:
                raise ValueError(f"unexpected mask bit: {mask_bit}")

        return int("".join(result), 2)


class Memory:
    def __init__(self):
        self._mask = Mask()
        self._memory: DefaultDict[int, int] = defaultdict(int)

    def set_mask(self, mask: str) -> None:
        self._mask.set(mask)

    def add(self, address: int, value: int) -> None:
        self._memory[address] = self._mask.apply(value)

    def sum(self) -> int:
        return sum(self._memory.values())


class Command(ABC):
    @staticmethod
    def from_line(line: str) -> Command:
        if line.startswith("mask"):
            return MaskCommand.from_line(line)
        elif line.startswith("mem"):
            return MemoryCommand.from_line(line)
        else:
            raise ValueError(f"unexpected command line: {line}")

    @abstractmethod
    def execute(self, memory: Memory) -> None:
        ...


@dataclass
class MaskCommand(Command):
    mask: str

    @staticmethod
    def from_line(line: str) -> MaskCommand:
        _, mask = line.split(" = ")
        return MaskCommand(mask)

    def execute(self, memory: Memory) -> None:
        memory.set_mask(self.mask)


@dataclass
class MemoryCommand(Command):
    address: int
    value: int

    @staticmethod
    def from_line(line: str) -> MemoryCommand:
        address, value = re.findall(r"\d+", line)
        return MemoryCommand(int(address), int(value))

    def execute(self, memory: Memory) -> None:
        memory.add(self.address, self.value)


def process_data(data: str) -> List[Command]:
    return [Command.from_line(line) for line in data.strip().split("\n")]


class Program:
    def __init__(self) -> None:
        self.mask = "X" * 36
        self.memory = Memory()

    def execute(self, commands: List[Command]) -> None:
        for command in commands:
            command.execute(self.memory)

    @property
    def memory_sum(self) -> int:
        return self.memory.sum()


def solve(task: str) -> int:
    """Sum all items in memory."""
    commands = process_data(task)
    program = Program()
    program.execute(commands)
    return program.memory_sum
