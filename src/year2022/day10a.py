"""2022 - Day 10 Part 1: Cathode-Ray Tube."""
from __future__ import annotations


class CPU:
    def __init__(self, instructions: list[int | None]) -> None:
        self.x = 1
        self.i = 0
        self.cycle = 1
        self.instructions = instructions
        self.pending: int | None = None

    @classmethod
    def from_task(cls, task: str) -> CPU:
        instructions: list[int | None] = []
        for line in task.splitlines():
            if line.startswith("noop"):
                instructions.append(None)
            else:
                _, value_str = line.split()
                instructions.append(int(value_str))
        return CPU(instructions)

    def step(self) -> None:
        if self.pending:
            self.x += self.pending
            self.pending = None
        else:
            if self.instructions[self.i]:
                self.pending = self.instructions[self.i]
            self.i += 1
        self.cycle += 1


def solve(task: str) -> int:
    cpu = CPU.from_task(task)
    checkpoints = {20, 60, 100, 140, 180, 220}
    total = 0

    while cpu.cycle < 220:
        cpu.step()
        if cpu.cycle in checkpoints:
            total += cpu.cycle * cpu.x

    return total
