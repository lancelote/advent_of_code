"""Day 7: Some Assembly Required."""
import re
from dataclasses import dataclass
from enum import Enum


PATTERN = re.compile(r"^(?:(?:(\w*) |)([A-Z]*) |)(\w*) -> (\w*)$")


class Gate(Enum):
    SIGNAL = 0
    NOT = 1
    RSHIFT = 2
    LSHIFT = 3
    AND = 4
    OR = 5


@dataclass
class Connection:
    gate: Gate
    out_wire: str
    input_a: str


@dataclass
class UnaryConnection(Connection):
    pass


@dataclass
class BinaryConnection(Connection):
    input_b: str


def process_data(data: str) -> dict[str, Connection]:
    connections: dict[str, Connection] = {}

    for line in data.strip().split("\n"):
        match = re.match(PATTERN, line)
        assert match

        connection: Connection
        a, gate, b, output = match.groups()

        if gate is None:
            connection = UnaryConnection(Gate.SIGNAL, output, b)
        elif gate == "NOT":
            connection = UnaryConnection(Gate.NOT, output, b)
        elif gate == "RSHIFT":
            connection = BinaryConnection(Gate.RSHIFT, output, a, b)
        elif gate == "LSHIFT":
            connection = BinaryConnection(Gate.LSHIFT, output, a, b)
        elif gate == "AND":
            connection = BinaryConnection(Gate.AND, output, a, b)
        elif gate == "OR":
            connection = BinaryConnection(Gate.OR, output, a, b)
        else:
            raise ValueError(f"unknown gate: {gate}")

        connections[output] = connection

    return connections


def solve(task: str, default_wire: str = "a") -> int:
    connections = process_data(task)
    cache: dict[str, int] = {}

    def get_value(wire: str) -> int:
        try:
            result = int(wire)
            cache[wire] = result
            return result
        except ValueError:
            pass

        if wire in cache:
            return cache[wire]

        result = 0
        connection = connections[wire]

        if isinstance(connection, UnaryConnection):
            if connection.gate is Gate.NOT:
                result = 65535 - get_value(connection.input_a)
            elif connection.gate is Gate.SIGNAL:
                result = get_value(connection.input_a)
            else:
                raise ValueError(f"unknown gate type: {connection.gate}")
        elif isinstance(connection, BinaryConnection):
            input_a = connection.input_a
            input_b = connection.input_b

            if connection.gate is Gate.RSHIFT:
                result = get_value(input_a) >> get_value(input_b)
            elif connection.gate is Gate.LSHIFT:
                result = get_value(input_a) << get_value(input_b)
            elif connection.gate is Gate.AND:
                result = get_value(input_a) & get_value(input_b)
            elif connection.gate is Gate.OR:
                result = get_value(input_a) | get_value(input_b)
            else:
                raise ValueError(f"unknown gate type: {connection.gate}")

        cache[wire] = result
        return result

    return get_value(default_wire)
