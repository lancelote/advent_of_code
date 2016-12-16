"""Day 7: Some Assembly Required.

This year, Santa brought little Bobby Tables a set of wires and bitwise logic
gates! Unfortunately, little Bobby is a little under the recommended age range,
and he needs help assembling the circuit.

Each wire has an identifier (some lowercase letters) and can carry a 16-bit
signal (a number from 0 to 65535). A signal is provided to each wire by a gate,
another wire, or some specific value. Each wire can only get a signal from one
source, but can provide its signal to multiple destinations. A gate provides no
signal until all of its inputs have a signal.

The included instructions booklet describes how to connect the parts together:
x AND y -> z means to connect wires x and y to an AND gate, and then connect
its output to wire z.

For example:

    `123 -> x` means that the signal 123 is provided to wire x.

    `x AND y -> z` means that the bitwise AND of wire x and wire y is provided
    to wire z.

    `p LSHIFT 2 -> q` means that the value from wire p is left-shifted by 2 and
    then provided to wire q.

    `NOT e -> f` means that the bitwise complement of the value from wire e is
    provided to wire f.

Other possible gates include OR (bitwise OR) and RSHIFT (right-shift). If, for
some reason, you'd like to emulate the circuit instead, almost all programming
languages (for example, C, JavaScript, or Python) provide operators for these
gates.

For example, here is a simple circuit:

    123 -> x
    456 -> y
    x AND y -> d
    x OR y -> e
    x LSHIFT 2 -> f
    y RSHIFT 2 -> g
    NOT x -> h
    NOT y -> i

After it is run, these are the signals on the wires:

    d: 72
    e: 507
    f: 492
    g: 114
    h: 65412
    i: 65079
    x: 123
    y: 456

In little Bobby's kit's instructions booklet (provided as your puzzle input),
what signal is ultimately provided to wire a?
"""

import re
from collections import namedtuple
from functools import lru_cache

PATTERN = re.compile(r'^(?:(?:(\w*) |)([A-Z]*) |)(\w*) -> (\w*)$')


def process_data(data):
    r"""Convert text data into list.

    Args:
        data: "NOT dq -> dr\nkg OR kf -> kh..."

    Returns:
        list: List of command namedtuples
    """
    processed_data = []
    command = namedtuple('Command', ['input_a', 'gate', 'input_b', 'output'])

    for line in data.strip().split('\n'):
        input_a, gate, input_b, output = re.match(PATTERN, line).groups()
        processed_data.append(command(input_a, gate, input_b, output))

    return processed_data


class HDict(dict):
    """Hashable dictionary for lru_cache compatibility."""

    def __hash__(self):
        """Calculate hash of items."""
        return hash(frozenset(self.items()))


@lru_cache(maxsize=500)
def get_value(wire, wires):
    """Recursive wire signal search.

    Args:
        wire (int or namedtuple): Wire signal or wire representation
        wires (dict): Collection of wires stored by wire label

    Returns:
        int: Wire signal
    """
    value = None

    try:
        return int(wire)
    except TypeError:
        pass

    if wire.gate is None:
        try:
            value = int(wire.input_b)
        except ValueError:
            value = get_value(wires[wire.input_b], wires)
    elif wire.gate == 'NOT':
        value = 65535 - get_value(wires[wire.input_b], wires)
    elif wire.gate == 'RSHIFT':
        value = get_value(wires[wire.input_a], wires) >> int(wire.input_b)
    elif wire.gate == 'LSHIFT':
        value = get_value(wires[wire.input_a], wires) << int(wire.input_b)
    elif wire.gate == 'AND':
        try:
            value_a = int(wire.input_a)
        except ValueError:
            value_a = get_value(wires[wire.input_a], wires)
        value = value_a & get_value(wires[wire.input_b], wires)
    elif wire.gate == 'OR':
        value = get_value(wires[wire.input_a], wires) | \
                get_value(wires[wire.input_b], wires)

    # wires[wire.output] = value
    return value


def solve(task):
    r"""Recursively process task data to compute wire 'a' value.

    Args:
        task: "NOT dq -> dr\nkg OR kf -> kh..."

    Returns:
        int: wire 'a' signal value
    """
    commands = process_data(task)
    wires = HDict()

    for command in commands:
        wires[command.output] = command

    return get_value(wires['a'], wires)
