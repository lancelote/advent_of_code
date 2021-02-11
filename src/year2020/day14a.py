"""2020 - Day 14 Part 1: Docking Data."""
from __future__ import annotations

import re
from collections import defaultdict
from dataclasses import dataclass
from typing import DefaultDict
from typing import List


class Command:
    @staticmethod
    def from_line(line: str) -> Command:
        if line.startswith("mask"):
            return MaskCommand.from_line(line)
        elif line.startswith("mem"):
            return MemoryCommand.from_line(line)
        else:
            raise ValueError(f"unexpected command line: {line}")


@dataclass
class MaskCommand(Command):
    mask: str

    @staticmethod
    def from_line(line: str) -> MaskCommand:
        _, mask = line.split(" = ")
        return MaskCommand(mask)


@dataclass
class MemoryCommand(Command):
    address: int
    value: int

    @staticmethod
    def from_line(line: str) -> MemoryCommand:
        address, value = re.findall(r"\d+", line)
        return MemoryCommand(int(address), int(value))


def process_data(data: str) -> List[Command]:
    return [Command.from_line(line) for line in data.strip().split("\n")]


class Program:
    def __init__(self) -> None:
        self.mask = "X" * 36
        self.memory: DefaultDict[int, int] = defaultdict(int)

    def execute(self, commands: List[Command]) -> None:
        for command in commands:
            if isinstance(command, MaskCommand):
                self.mask = command.mask
            elif isinstance(command, MemoryCommand):
                self.add(command.address, command.value)

    def add(self, address: int, value: int) -> None:
        value = self.apply_mask(value)
        self.memory[address] = value

    def apply_mask(self, value: int) -> int:
        str_value = bin(value)[2:].rjust(36, "0")
        result = []

        for bit, mask_bit in zip(str_value, self.mask):
            if mask_bit == "X":
                result.append(bit)
            elif mask_bit == "0":
                result.append("0")
            elif mask_bit == "1":
                result.append("1")
            else:
                raise ValueError(f"unexpected mask bit: {mask_bit}")

        return int("".join(result), 2)

    @property
    def memory_sum(self) -> int:
        return sum(self.memory.values())


def solve(task: str) -> int:
    """Sum all items in memory."""
    commands = process_data(task)
    program = Program()
    program.execute(commands)
    return program.memory_sum
