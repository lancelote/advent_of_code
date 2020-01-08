"""2019 - Day 8 Part 1: Space Image Format."""

from typing import List


def parse_layers(data: str, n: int) -> List[List[int]]:
    """Get all layers from raw data."""
    return [[int(x) for x in data[i:i + n]] for i in range(0, len(data), n)]


def solve(task: str) -> int:
    """Ensure the image is not corrupted."""
    layers = parse_layers(task.strip(), 25 * 6)
    min_zero_layers = min(layers, key=lambda layer: layer.count(0))
    return min_zero_layers.count(1) * min_zero_layers.count(2)
