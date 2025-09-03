"""2015 - Day 7 Part 1: Some Assembly Required."""

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


class Solution:
    def __init__(self, connections: dict[str, Connection]) -> None:
        self.connections: dict[str, Connection] = connections
        self.cache: dict[str, int] = {}

    def get_value(self, wire: str) -> int:
        try:
            result = int(wire)
            self.cache[wire] = result
            return result
        except ValueError:
            pass

        if wire in self.cache:
            return self.cache[wire]

        result = 0
        connection = self.connections[wire]

        match connection:
            case UnaryConnection():
                match connection.gate:
                    case Gate.NOT:
                        result = 65535 - self.get_value(connection.input_a)
                    case Gate.SIGNAL:
                        result = self.get_value(connection.input_a)
                    case unknown_gate:
                        raise ValueError(f"unknown gate type: {unknown_gate}")
            case BinaryConnection():
                in_a = connection.input_a
                in_b = connection.input_b

                match connection.gate:
                    case Gate.RSHIFT:
                        result = self.get_value(in_a) >> self.get_value(in_b)
                    case Gate.LSHIFT:
                        result = self.get_value(in_a) << self.get_value(in_b)
                    case Gate.AND:
                        result = self.get_value(in_a) & self.get_value(in_b)
                    case Gate.OR:
                        result = self.get_value(in_a) | self.get_value(in_b)
                    case unknown_gate:
                        raise ValueError(f"unknown gate type: {unknown_gate}")
            case _:
                raise ValueError("unknown connection type")

        self.cache[wire] = result
        return result


def solve(task: str) -> int:
    connections = process_data(task)
    return Solution(connections).get_value("a")
