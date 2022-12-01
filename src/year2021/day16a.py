"""2021 - Day 16 Part 1: Packet Decoder."""
from __future__ import annotations

from dataclasses import dataclass
from functools import reduce
from operator import mul
from typing import NamedTuple


class ValueChunk(NamedTuple):
    prefix: str
    body: str


def hex_to_bin(hex_num: str) -> str:
    assert len(hex_num) == 1

    decimal = int(hex_num, base=16)
    binary = bin(decimal)
    return binary[2:].rjust(4, "0")


@dataclass
class Packet:
    version: int
    type_id: int

    def evaluate(self) -> int:
        return 0


@dataclass
class LiteralPacket(Packet):
    value: int

    def evaluate(self) -> int:
        return self.value


@dataclass
class OperatorPacket(Packet):
    sub_packets: list[Packet]

    def evaluate(self) -> int:
        if self.type_id == 0:
            return sum(x.evaluate() for x in self.sub_packets)
        elif self.type_id == 1:
            return reduce(mul, [x.evaluate() for x in self.sub_packets])
        elif self.type_id == 2:
            return min(x.evaluate() for x in self.sub_packets)
        elif self.type_id == 3:
            return max(x.evaluate() for x in self.sub_packets)
        elif self.type_id == 5:
            first, second = self.sub_packets
            return 1 if first.evaluate() > second.evaluate() else 0
        elif self.type_id == 6:
            first, second = self.sub_packets
            return 1 if first.evaluate() < second.evaluate() else 0
        elif self.type_id == 7:
            first, second = self.sub_packets
            return 1 if first.evaluate() == second.evaluate() else 0
        else:
            raise ValueError(f"unknown type id: {self.type_id}")


class BITS:
    def __init__(self, bin_data: str) -> None:
        self.data = bin_data
        self.pointer = 0

    @classmethod
    def from_hex(cls, hex_line: str) -> BITS:
        return cls("".join(hex_to_bin(x) for x in hex_line))

    def read_version(self) -> int:
        return self.read_int(bit_length=3)

    def read_type_id(self) -> int:
        return self.read_int(bit_length=3)

    def read_value(self) -> int:
        bin_value: list[str] = []
        has_next_chunk = True

        while has_next_chunk:
            chunk = self.read_value_chunk()
            bin_value.append(chunk.body)
            if chunk.prefix == "0":
                has_next_chunk = False

        return int("".join(bin_value), base=2)

    def read_value_chunk(self) -> ValueChunk:
        prefix = self.read_bits(1)
        body = self.read_bits(4)
        return ValueChunk(prefix, body)

    def read_length_type_id(self) -> str:
        return self.read_bits(1)

    def read_sub_packets_len(self) -> int:
        return self.read_int(bit_length=15)

    def read_sub_packets_num(self) -> int:
        return self.read_int(bit_length=11)

    def read_packets_until(self) -> list[Packet]:
        sub_packets_len = self.read_sub_packets_len()
        limit = self.pointer + sub_packets_len
        sub_packets = []

        while self.pointer < limit:
            sub_packets.append(self.read_packet())

        return sub_packets

    def read_next_n_packets(self) -> list[Packet]:
        sub_packets_num = self.read_sub_packets_num()
        return [self.read_packet() for _ in range(sub_packets_num)]

    def read_packet(self) -> Packet:
        version = self.read_version()
        type_id = self.read_type_id()

        if type_id == 4:
            value = self.read_value()
            return LiteralPacket(version, type_id, value)
        else:
            length_type_id = self.read_length_type_id()
            if length_type_id == "0":
                sub_packets = self.read_packets_until()
            else:
                sub_packets = self.read_next_n_packets()

            return OperatorPacket(version, type_id, sub_packets)

    def read_bits(self, n: int) -> str:
        bits = self.data[self.pointer : self.pointer + n]
        self.pointer += n
        return bits

    def read_int(self, bit_length: int) -> int:
        bits = self.read_bits(bit_length)
        return int(bits, base=2)


def sum_versions(packet: Packet) -> int:
    if isinstance(packet, LiteralPacket):
        return packet.version

    assert isinstance(packet, OperatorPacket)
    return packet.version + sum(sum_versions(x) for x in packet.sub_packets)


def solve(task: str) -> int:
    system = BITS.from_hex(task)
    top_packet = system.read_packet()
    return sum_versions(top_packet)
