"""2021 - Day 16 Part 1: Packet Decoder."""

import pytest

from src.year2021.day16a import BITS, LiteralPacket, OperatorPacket, solve


def test_literal_packet():
    bits = BITS.from_hex("D2FE28")
    packet = bits.read_packet()

    assert packet.version == 6
    assert packet.type_id == 4
    assert isinstance(packet, LiteralPacket)
    assert packet.value == 2021


def test_operator_packet_1():
    bits = BITS.from_hex("38006F45291200")
    packet = bits.read_packet()

    assert packet.version == 1
    assert packet.type_id == 6
    assert isinstance(packet, OperatorPacket)
    assert len(packet.sub_packets) == 2

    sub_packet_1, sub_packet_2 = packet.sub_packets

    assert sub_packet_1.version == 6
    assert sub_packet_1.type_id == 4
    assert isinstance(sub_packet_1, LiteralPacket)
    assert sub_packet_1.value == 10

    assert sub_packet_2.version == 2
    assert sub_packet_2.type_id == 4
    assert isinstance(sub_packet_2, LiteralPacket)
    assert sub_packet_2.value == 20


def test_operator_packet_2():
    bits = BITS.from_hex("EE00D40C823060")
    packet = bits.read_packet()

    assert packet.version == 7
    assert packet.type_id == 3
    assert isinstance(packet, OperatorPacket)
    assert len(packet.sub_packets) == 3

    sub_packet_1, sub_packet_2, sub_packet_3 = packet.sub_packets

    assert sub_packet_1.version == 2
    assert sub_packet_1.type_id == 4
    assert isinstance(sub_packet_1, LiteralPacket)
    assert sub_packet_1.value == 1

    assert sub_packet_2.version == 4
    assert sub_packet_2.type_id == 4
    assert isinstance(sub_packet_2, LiteralPacket)
    assert sub_packet_2.value == 2

    assert sub_packet_3.version == 1
    assert sub_packet_3.type_id == 4
    assert isinstance(sub_packet_3, LiteralPacket)
    assert sub_packet_3.value == 3


@pytest.mark.parametrize(
    "task,version_sum",
    [
        ("D2FE28", 6),
        ("38006F45291200", 9),
        ("8A004A801A8002F478", 16),
        ("620080001611562C8802118E34", 12),
        ("C0015000016115A2E0802F182340", 23),
        ("A0016C880162017C3686B18A3D4780", 31),
    ],
)
def test_solve(task, version_sum):
    assert solve(task) == version_sum
