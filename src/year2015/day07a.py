"""Day 7: Some Assembly Required."""
import re
from functools import lru_cache
from typing import NamedTuple


PATTERN = re.compile(r"^(?:(?:(\w*) |)([A-Z]*) |)(\w*) -> (\w*)$")


class Command(NamedTuple):
    input_a: str
    gate: str
    input_b: str
    output: str


def process_data(data: str) -> list[Command]:
    r"""Convert text data into list.

    Args:
        data: "NOT dq -> dr\nkg OR kf -> kh..."

    Returns:
        list: List of command namedtuples
    """
    processed_data = []

    for line in data.strip().split("\n"):
        match = re.match(PATTERN, line)
        assert match

        input_a, gate, input_b, output = match.groups()
        processed_data.append(Command(input_a, gate, input_b, output))

    return processed_data


class HDict(dict[str, Command | int]):
    """Hashable dictionary for lru_cache compatibility."""

    def __hash__(self) -> int:
        """Calculate hash of items."""
        return hash(frozenset(self.items()))


@lru_cache(maxsize=500)
def get_value(wire: int | Command, wires: HDict) -> int:
    """Recursive wire signal search.

    Args:
        wire (int or namedtuple): Wire signal or wire representation
        wires (dict): Collection of wires stored by wire label

    Returns:
        int: Wire signal
    """
    value = 0

    if isinstance(wire, int):
        return wire

    if wire.gate is None:
        try:
            value = int(wire.input_b)
        except ValueError:
            value = get_value(wires[wire.input_b], wires)
    elif wire.gate == "NOT":
        value = 65535 - get_value(wires[wire.input_b], wires)
    elif wire.gate == "RSHIFT":
        value = get_value(wires[wire.input_a], wires) >> int(wire.input_b)
    elif wire.gate == "LSHIFT":
        value = get_value(wires[wire.input_a], wires) << int(wire.input_b)
    elif wire.gate == "AND":
        try:
            value_a = int(wire.input_a)
        except ValueError:
            value_a = get_value(wires[wire.input_a], wires)
        value = value_a & get_value(wires[wire.input_b], wires)
    elif wire.gate == "OR":
        value = get_value(wires[wire.input_a], wires) | get_value(
            wires[wire.input_b], wires
        )

    # wires[wire.output] = value
    return value


def solve(task: str) -> int:
    r"""Recursively process task data to compute wire 'a' value.

    Args:
        task: "NOT dq -> dr\nkg OR kf -> kh..."

    Returns:
        int: wire 'a' signal value
    """
    commands = process_data(task)
    wires: HDict = HDict()

    for command in commands:
        wires[command.output] = command

    return get_value(wires["a"], wires)
