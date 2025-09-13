"""2015 - Day 15 Part 1: Science for Hungry People."""

from src.year2015.day15a import Ingredient
from src.year2015.day15a import get_score
from src.year2015.day15a import solve


def test_get_score():
    assert (
        get_score(
            [44, 56],
            [
                Ingredient(-1, -2, 6, 3, 8),
                Ingredient(2, 3, -2, -1, 3),
            ],
        )
        == 62842880
    )


def test_solve():
    task = """Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3"""
    assert solve(task) == 62842880
