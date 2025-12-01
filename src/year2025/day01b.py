"""2025 - Day 1 Part 2: Secret Entrance"""

from src.year2025.day01a import Direction
from src.year2025.day01a import Rotation
from src.year2025.day01a import process_data


def get_password(rotations: list[Rotation]) -> int:
    zero_count = 0
    dial = 50

    for rotation in rotations:
        shift = rotation.distance % 100
        complete_circles = rotation.distance // 100

        zero_count += complete_circles

        if rotation.direction is Direction.L:
            shift *= -1

        raw_dial = dial + shift

        if dial != 0 and (raw_dial <= 0 or raw_dial >= 100):
            zero_count += 1

        dial = raw_dial % 100

    return zero_count


def solve(task: str) -> int:
    rotations = process_data(task)
    return get_password(rotations)
