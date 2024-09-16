"""2021 - Day 16 Part 2: Packet Decoder."""

import pytest

from src.year2021.day16b import solve


@pytest.mark.parametrize(
    "task,evaluation_result",
    [
        ("C200B40A82", 3),
        ("04005AC33890", 54),
        ("880086C3E88112", 7),
        ("CE00C43D881120", 9),
        ("D8005AC2A8F0", 1),
        ("F600BC2D8F", 0),
        ("9C005AC2F8F0", 0),
        ("9C0141080250320F1802104A08", 1),
    ],
)
def test_solve(task, evaluation_result):
    assert solve(task) == evaluation_result
