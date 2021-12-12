"""2020 - Day 8 Part 1: Handheld Halting."""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import List
from typing import Tuple


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
    op: Operation
    arg: int

    @classmethod
    def from_line(cls, line: str) -> Instruction:
        op, arg = line.split()
        return cls(Operation.from_str(op), int(arg))

    def swap(self) -> None:
        if self.op is Operation.NOP:
            self.op = Operation.JMP
        elif self.op is Operation.JMP:
            self.op = Operation.NOP
        else:
            raise ValueError(f"swap attempt on {self.op}")

    @property
    def is_swapable(self) -> bool:
        return self.op is Operation.NOP or self.op is Operation.JMP


def process_data(task: str) -> List[Instruction]:
    return [Instruction.from_line(line) for line in task.strip().split("\n")]


def run(instructions: List[Instruction]) -> Tuple[bool, int]:
    i = 0
    acc = 0
    seen = set()
    graceful = True

    while i < len(instructions):
        current = instructions[i]

        if i in seen:
            graceful = False
            break
        else:
            seen.add(i)

        if current.op is Operation.ACC:
            acc += current.arg
            i += 1
        elif current.op is Operation.JMP:
            i += current.arg
        elif current.op is Operation.NOP:
            i += 1
        else:
            raise ValueError(f"unknown operation {current.op}")

    return graceful, acc


def solve(task: str) -> int:
    """What is the value of accumulator?"""
    instructions = process_data(task)
    _, acc = run(instructions)
    return acc
