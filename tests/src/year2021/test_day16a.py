"""2021 - Day 16 Part 1: Packet Decoder."""

from src.year2021.day16a import BITS
from src.year2021.day16a import LiteralPacket


def test_literal_packet():
    bits = BITS.from_hex("D2FE28")
    packet = bits.read_packet()

    assert packet.version == 6
    assert packet.type_id == 4
    assert isinstance(packet, LiteralPacket)
    assert packet.value == 2021
