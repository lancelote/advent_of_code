"""2017 - Day 10 Part 2: Knot Hash."""
from functools import reduce
from operator import xor

from src.year2017.day10a import Rope


def process_data(data: str) -> list[int]:
    """Convert each character into ASCII byte code."""
    return [ord(char) for char in data.strip()]


def split(sequence: list[int], chunk: int) -> list[list[int]]:
    """Split sequence into equal segments of the given length."""
    return [sequence[i * chunk : (i + 1) * chunk] for i in range(chunk)]


def compress(sparse_hash: list[int], chunk: int = 16) -> list[int]:
    """Compress sparse hash into dense by XORing each 16 items."""
    return [reduce(xor, segment) for segment in split(sparse_hash, chunk)]


def to_hex(number: int) -> str:
    """Convert number to hex and made a basic formatting."""
    return hex(number)[2:].zfill(2)


def solve(task: str) -> str:
    """Find Knot Hash of the given input."""
    rope = Rope()
    lengths = process_data(task) + [17, 31, 73, 47, 23]
    for _ in range(64):
        for length in lengths:
            rope.reverse(length)
            rope.move(length)
    sparse_hash = rope.nodes
    dense_hash = compress(sparse_hash)
    return "".join(to_hex(number) for number in dense_hash)
