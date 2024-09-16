"""2022 - Day 5 Part 1: Supply Stacks."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TypeAlias

Stack: TypeAlias = list[str]


@dataclass
class Command:
    count: int
    from_stack: int
    to_stack: int

    @classmethod
    def from_line(cls, line: str) -> Command:
        _, count, _, from_stack, _, to_stack = line.split()
        return Command(int(count), int(from_stack) - 1, int(to_stack) - 1)


def process_data(task: str) -> tuple[list[Stack], list[Command]]:
    lines = task.splitlines()

    n_stacks = 0
    commands_start_i = 0

    for i, line in enumerate(lines):
        if line.strip().startswith("1"):
            n_stacks = len(line.strip().split())
            commands_start_i = i + 2

    commands = []
    for i in range(commands_start_i, len(lines)):
        commands.append(Command.from_line(lines[i]))

    stacks: list[Stack] = [[] for _ in range(n_stacks)]

    for i in range(commands_start_i - 3, -1, -1):
        for j in range(n_stacks):
            crate_i = 1 + 4 * j
            if len(lines[i]) > crate_i and lines[i][crate_i] != " ":
                stacks[j].append(lines[i][crate_i])

    return stacks, commands


def execute_9000(stacks: list[Stack], commands: list[Command]) -> None:
    for command in commands:
        old_stack = stacks[command.from_stack]
        sub_stack = old_stack[-1 : -command.count - 1 : -1]
        stacks[command.from_stack] = old_stack[: -command.count]
        stacks[command.to_stack].extend(sub_stack)


def solve(task: str) -> str:
    stacks, commands = process_data(task)
    execute_9000(stacks, commands)
    return "".join(stack[-1] for stack in stacks)
