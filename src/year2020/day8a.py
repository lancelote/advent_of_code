"""2020 - Day 8 Part 1: Handheld Halting."""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import List


class Operation(Enum):
    NOP = 0
    ACC = 1
    JMP = 2

    @classmethod
    def from_str(cls, op: str) -> Operation:
        if op == "nop":
            return cls.NOP
        elif op == "acc":
            return cls.ACC
        elif op == "jmp":
            return cls.JMP
        else:
            raise ValueError(f"unknown operation: {op}")


@dataclass
class Instruction:
    operation: Operation
    argument: int
    seen: bool = False

    @classmethod
    def from_line(cls, line: str) -> Instruction:
        op, arg = line.split()
        return cls(Operation.from_str(op), int(arg))


def process_data(task: str) -> List[Instruction]:
    return [Instruction.from_line(line) for line in task.strip().split("\n")]


def run(instructions: List[Instruction]) -> int:
    i = 0
    acc = 0

    while True:
        current = instructions[i]

        if current.seen:
            break
        else:
            current.seen = True

        if current.operation is Operation.ACC:
            acc += current.argument
            i += 1
        elif current.operation is Operation.JMP:
            i += current.argument
        elif current.operation is Operation.NOP:
            i += 1
        else:
            raise ValueError(f"unknown operation {current.operation}")

    return acc


def solve(task: str) -> int:
    """What is the value of accumulator?"""
    instructions = process_data(task)
    acc = run(instructions)
    return acc
