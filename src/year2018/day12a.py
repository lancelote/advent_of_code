"""Day 12 Part 1: Subterranean Sustainability."""

from enum import Enum
from typing import TypeAlias


class Pot(Enum):
    """Represent a pot with (#) or without (.) a plant."""

    EMPTY = "."
    PLANT = "#"


POT_ID = int
GEN: TypeAlias = dict[POT_ID, Pot]
PATTERN: TypeAlias = str
PATTERNS: TypeAlias = dict[PATTERN, Pot]


def process_data(task: str) -> tuple[GEN, PATTERNS]:
    """Convert raw data into initial generation and the list of patterns."""
    data_lines = task.strip().split("\n")
    raw_initial_state = data_lines[0].split()[2]

    start_generation: GEN = dict()
    for i, pot in enumerate(raw_initial_state):
        if pot == "#":
            start_generation[i] = Pot.PLANT

    patterns: PATTERNS = dict()
    for line in data_lines[2:]:
        pattern, _, pot = line.split()
        if pot == "#":
            patterns[pattern] = Pot.PLANT
        elif pot == ".":
            patterns[pattern] = Pot.EMPTY
        else:
            raise ValueError(f"Unknown plot state: {pot}")

    return start_generation, patterns


def get_pattern(generation: GEN, i: int) -> PATTERN:
    """Get around pattern for a given pot."""
    indexes = [i - 2, i - 1, i, i + 1, i + 2]
    return "".join(generation.get(index, Pot.EMPTY).value for index in indexes)


def print_plants(generation: GEN, generation_id: int = 0) -> None:
    """Print current plants layout."""
    start = min(generation.keys())
    end = max(generation.keys())
    representation = ""

    for i in range(start, end + 1):
        representation += generation.get(i, Pot.EMPTY).value

    print(str(generation_id).rjust(3), representation)


def get_new_generation(generation: GEN, patterns: PATTERNS) -> GEN:
    """Mutate current generation and get the next one."""
    new_generation: GEN = dict()
    plant_ids = generation.keys()
    min_plant_id = min(plant_ids)
    max_plant_id = max(plant_ids)

    for i in range(min_plant_id - 2, max_plant_id + 2):
        pattern = get_pattern(generation, i)
        if patterns.get(pattern, Pot.EMPTY) is Pot.PLANT:
            new_generation[i] = Pot.PLANT

    return new_generation


def solve(task: str) -> int:
    """Find the sum of all pots id with plants after 20 generations."""
    generation, patterns = process_data(task)
    for _ in range(20):  # generations
        new_generation = get_new_generation(generation, patterns)
        generation = new_generation

    return sum(generation.keys())
