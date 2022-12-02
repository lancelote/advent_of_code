"""2015 - Day 2 Part 2: I Was Told There Would Be No Math."""
from src.year2015.day02a import process_data


def solve(task: str) -> int:
    boxes = process_data(task)
    return sum(
        2 * (sum(box) - max(box)) + box.width * box.height * box.length
        for box in boxes
    )
