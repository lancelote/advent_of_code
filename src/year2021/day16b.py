"""2021 - Day 16 Part 2: Packet Decoder."""
from src.year2021.day16a import BITS


def solve(task: str) -> int:
    system = BITS.from_hex(task)
    top_packet = system.read_packet()
    return top_packet.evaluate()
