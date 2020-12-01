"""2019 - Day 14 Part 1: Space Stoichiometry."""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from typing import DefaultDict, Dict, List, Optional

ChemicalName = str


@dataclass
class ChemicalRecipe:
    """Recipe contains of the chemical name and the quantity."""

    quantity: int
    name: ChemicalName

    @classmethod
    def from_str(cls, string: str):
        """Convert raw string (e.g. 8 "NLTCF") to ChemicalRecipe."""
        quantity, name = string.split()
        return cls(int(quantity), name)


@dataclass
class Reaction:
    """Contains of quantity of output and the desired inputs."""

    quantity: int
    ins: List[ChemicalRecipe]


REACTIONS = Dict[ChemicalName, Reaction]


def get_multiplier(target: int, reaction: int) -> int:
    """How many times to call reaction to produce target quantity."""
    if target / reaction < 0:  # Reaction made more than required
        return 1
    elif target % reaction != 0:
        return target // reaction + 1
    else:
        return target // reaction


class Factory:
    """FUEL factory."""

    def __init__(self, reactions: Optional[REACTIONS] = None):
        """Create factory from reactions dictionary."""
        self._to_produce: DefaultDict[ChemicalName, int] = defaultdict(int)
        self._reactions = reactions if reactions else dict()
        self.ore: int = 0

    @classmethod
    def from_raw_data(cls, data: str) -> Factory:
        """Create chemical factory from the raw data."""
        reactions = dict()

        for line in data.strip().split("\n"):
            ins_str, out_str = line.split(" => ")
            out = ChemicalRecipe.from_str(out_str)
            ins = [
                ChemicalRecipe.from_str(item) for item in ins_str.split(", ")
            ]
            reaction = Reaction(out.quantity, ins)

            assert out.name not in reactions, f"known output {out.name}"

            reactions[out.name] = reaction

        return cls(reactions)

    def add_to_production(self, chemical: ChemicalName, quantity: int):
        """Add new chemical to production list."""
        if chemical == "ORE":
            self.ore += quantity
        else:
            self._to_produce[chemical] += quantity

    def produce(self):
        """Start producing."""
        while self._to_produce:
            chemical_name, desired_quantity = self._to_produce.popitem()
            reaction = self._reactions[chemical_name]
            multiplier = get_multiplier(desired_quantity, reaction.quantity)

            for chemical_recipe in reaction.ins:
                self.add_to_production(
                    chemical_recipe.name, chemical_recipe.quantity * multiplier
                )


def solve(task: str) -> int:
    """Find out how many ore is needed to produce 1 FUEL."""
    factory = Factory.from_raw_data(task)
    factory.add_to_production("FUEL", 1)
    factory.produce()
    return factory.ore
