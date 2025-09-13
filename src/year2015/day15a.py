"""2015 - Day 15 Part 1: Science for Hungry People."""

import re
from dataclasses import dataclass
from typing import Self


@dataclass
class Ingredient:
    capacity: int
    durability: int
    flavor: int
    texture: int
    calories: int

    @classmethod
    def from_line(cls, line: str) -> Self:
        match: list[str] | None = re.findall(r"(-?\d+)", line)

        assert match is not None
        assert len(match) == 5

        return cls(*[int(x) for x in match])


def process_data(task: str) -> list[Ingredient]:
    return [Ingredient.from_line(line) for line in task.splitlines()]


def get_score(spoons: list[int], ingredients: list[Ingredient]) -> int:
    assert len(spoons) == len(ingredients)

    capacity = 0
    durability = 0
    flavor = 0
    texture = 0

    for spoon, ingredient in zip(spoons, ingredients):
        capacity += spoon * ingredient.capacity
        durability += spoon * ingredient.durability
        flavor += spoon * ingredient.flavor
        texture += spoon * ingredient.texture

    capacity = max(0, capacity)
    durability = max(0, durability)
    flavor = max(0, flavor)
    texture = max(0, texture)

    return capacity * durability * flavor * texture


def get_calories(spoons: list[int], ingredients: list[Ingredient]) -> int:
    total = 0

    for count, ingredient in zip(spoons, ingredients):
        total += count * ingredient.calories

    return total


def solve(task: str, limit_calories: bool = False) -> int:
    ingredients = process_data(task)
    max_score = 0
    spoons = [0] * len(ingredients)

    def recurse(limit: int, depth: int) -> None:
        nonlocal max_score

        for x in range(limit):
            spoons[len(ingredients) - depth - 1] = x

            if depth == 0:
                if sum(spoons) != 100:
                    continue

                if limit_calories and get_calories(spoons, ingredients) != 500:
                    continue

                score = get_score(spoons, ingredients)
                max_score = max(max_score, score)
            else:
                recurse(limit - x, depth - 1)

    recurse(101, len(ingredients) - 1)
    return max_score
