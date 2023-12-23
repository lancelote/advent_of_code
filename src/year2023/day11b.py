"""2023 - Day 11 Part 2: Cosmic Expansion"""
from src.year2023.day11a import StarMap


def solve(task: str) -> int:
    sm = StarMap.from_text(task, age=1_000_000)
    return sm.total_path
