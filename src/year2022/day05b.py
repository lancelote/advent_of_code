"""2022 - Day 5 Part 2: Supply Stacks."""

from src.year2022.day05a import Command, Stack, process_data


def execute_9001(stacks: list[Stack], commands: list[Command]) -> None:
    for command in commands:
        old_stack = stacks[command.from_stack]
        sub_stack = old_stack[-command.count :]
        stacks[command.from_stack] = old_stack[: -command.count]
        stacks[command.to_stack].extend(sub_stack)


def solve(task: str) -> str:
    stacks, commands = process_data(task)
    execute_9001(stacks, commands)
    return "".join(stack[-1] for stack in stacks)
