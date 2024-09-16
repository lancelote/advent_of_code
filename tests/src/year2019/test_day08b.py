"""2019 - Day 8 Part 2: Space Image Format tests."""

from src.year2019.day08b import decode_image
from src.year2019.day08b import parse_layers


def test_decode_image():
    size = 2 * 2
    task = "0222112222120000"
    layers = parse_layers(task, size)

    assert decode_image(layers) == [" ", "#", "#", " "]
