"""2019 - Day 8 Part 2: Space Image Format."""
from src.year2019.day08a import parse_layers


def find_top(layers: list[list[int]], pixel: int) -> str:
    """Find the given visible pixel number color."""
    for layer in layers:
        if layer[pixel] == 0:  # black
            return " "
        elif layer[pixel] == 1:  # white
            return "#"
        elif layer[pixel] == 2:  # transparent
            continue
        raise ValueError(f"unexpected pixel color {layer[pixel]}")
    raise ValueError(f"no visible pixel at position {pixel}")


def decode_image(layers: list[list[int]]) -> list[str]:
    """Get visible pixels from every layer."""
    return [find_top(layers, i) for i in range(len(layers[0]))]


def print_image(image: list[str], cols: int) -> None:
    """Print the image splitting by rows."""
    for i, pixel in enumerate(image):
        if i % cols == 0:
            print()
        print(pixel, end="")


def solve(task: str) -> int:
    """Find the image message."""
    cols = 25
    rows = 6
    size = cols * rows
    layers = parse_layers(task, size)
    image = decode_image(layers)
    print_image(image, cols)
    print()
    return 0
