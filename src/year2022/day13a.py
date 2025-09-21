"""2022 - Day 13 Part 1: Distress Signal."""

from __future__ import annotations

import ast

type Packet = list[int | Packet]
type Pair = tuple[Packet, Packet]


def parse_packet(line: str) -> Packet:
    packet: Packet = ast.literal_eval(line)
    return packet


def compare(packet1: Packet | int, packet2: Packet | int) -> int:
    lst1: Packet
    lst2: Packet

    if isinstance(packet1, int) and isinstance(packet2, int):
        return packet1 - packet2

    if isinstance(packet1, int):
        lst1 = [packet1]
    else:
        lst1 = packet1

    if isinstance(packet2, int):
        lst2 = [packet2]
    else:
        lst2 = packet2

    for x1, x2 in zip(lst1, lst2, strict=False):
        item_result = compare(x1, x2)
        if item_result != 0:
            return item_result

    return len(lst1) - len(lst2)


def parse_pairs(task: str) -> list[Pair]:
    result: list[Pair] = []

    for pair_str in task.split("\n\n"):
        packet1_line, packet2_line = pair_str.splitlines()

        packet1 = parse_packet(packet1_line)
        packet2 = parse_packet(packet2_line)

        result.append((packet1, packet2))

    return result


def solve(task: str) -> int:
    indices: list[int] = []

    for i, pair in enumerate(parse_pairs(task), start=1):
        packet1, packet2 = pair
        if compare(packet1, packet2) <= 0:
            indices.append(i)

    return sum(indices)
