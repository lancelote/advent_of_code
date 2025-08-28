"""2022 - Day 13 Part 2: Distress Signal."""

from __future__ import annotations

from functools import cmp_to_key

from src.year2022.day13a import Packet, compare, parse_packet


def parse_packets(task: str) -> list[Packet]:
    result: list[Packet] = []

    for pair_str in task.split("\n\n"):
        packet1_line, packet2_line = pair_str.splitlines()

        packet1 = parse_packet(packet1_line)
        packet2 = parse_packet(packet2_line)

        result.append(packet1)
        result.append(packet2)

    return result


def solve(task: str) -> int:
    packets = parse_packets(task)

    divider1 = parse_packet("[[2]]")
    divider2 = parse_packet("[[6]]")

    packets.append(divider1)
    packets.append(divider2)

    packets.sort(key=cmp_to_key(compare))

    divider1_index = packets.index(divider1) + 1
    divider2_index = packets.index(divider2) + 1

    return divider1_index * divider2_index
