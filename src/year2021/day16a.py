"""2021 - Day 16 Part 1: Packet Decoder."""
from __future__ import annotations

from dataclasses import dataclass
from typing import NamedTuple


class Chunk(NamedTuple):
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


@dataclass
class LiteralPacket(Packet):
    value: int


@dataclass
class OperatorPacket(Packet):
    sub_packets: list[Packet]


class BITS:
    def __init__(self, bin_data: str) -> None:
        self.data = bin_data
        self.pointer = 0

    @classmethod
    def from_hex(cls, hex_line: str) -> BITS:
        return cls("".join(hex_to_bin(x) for x in hex_line))

    def read_version(self) -> int:
        version = int(self.data[self.pointer : self.pointer + 3], base=2)
        self.pointer += 3
        return version

    def read_type_id(self) -> int:
        return self.read_version()

    def read_value(self) -> int:
        bin_value: list[str] = []
        has_next_chunk = True

        while has_next_chunk:
            chunk = self.read_chunk()
            bin_value.append(chunk.body)
            if chunk.prefix == "0":
                has_next_chunk = False

        return int("".join(bin_value), base=2)

    def read_chunk(self) -> Chunk:
        prefix = self.data[self.pointer]
        body = self.data[self.pointer + 1 : self.pointer + 5]
        self.pointer += 5
        return Chunk(prefix, body)

    def read_length_type_id(self) -> str:
        return self.data[self.pointer]

    def read_packet(self) -> LiteralPacket:
        version = self.read_version()
        type_id = self.read_type_id()

        if type_id == 4:
            value = self.read_value()
            return LiteralPacket(version, type_id, value)
        else:
            length_type_id = self.read_length_type_id()
            if length_type_id == "0":
                ...
            else:
                ...


def sum_versions(packet: Packet) -> int:
    ...


def solve(task: str) -> int:
    bits = BITS.from_hex(task)
    top_packet = bits.read_packet()
    return sum_versions(top_packet)
