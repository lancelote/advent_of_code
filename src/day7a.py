# coding=utf-8

"""
--- Day 7: Some Assembly Required ---

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
from collections import defaultdict, namedtuple

PATTERN = re.compile(r'^(?:(?:(\w*) |)([A-Z]*) |)(\w*) -> (\w*)$')


def process_data(data):
    processed_data = []
    command = namedtuple('Command', ['input_a', 'gate', 'input_b', 'output'])

    for line in data.strip().split('\n'):
        a, gate, b, output = re.match(PATTERN, line).groups()
        b = int(b) if gate in (None, 'LSHIFT', 'RSHIFT') else b
        processed_data.append(command(a, gate, b, output))

    return processed_data


class Signal(object):

    def __init__(self, a=None, gate=None, b=None, output=None):
        self.a = a
        self.gate = gate
        self.b = b
        self.output = output

    def get_value(self, signals):
        __value = None

        if self.gate is None:
            __value = self.b
        elif self.gate == 'AND':
            __value = signals[self.a].get_value(signals) & signals[self.b].get_value(signals)
        elif self.gate == 'OR':
            __value = signals[self.a].get_value(signals) | signals[self.b].get_value(signals)
        elif self.gate == 'LSHIFT':
            __value = signals[self.a].get_value(signals) << self.b
        elif self.gate == 'RSHIFT':
            __value = signals[self.a].get_value(signals) >> self.b
        elif self.gate == 'NOT':
            __value = 65535 - signals[self.b].get_value(signals)
        return __value


def solve(task):
    signals = dict()
    commands = process_data(task)
    for command in commands:
        signals[command.output] = Signal(*command)
    return signals['a'].get_value(signals)
