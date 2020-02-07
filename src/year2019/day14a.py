"""2019 - Day 14 Part 1: Space Stoichiometry."""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from typing import Dict, List, DefaultDict, Optional


ChemicalName = str


@dataclass
class ChemicalRecipe:
    quantity: int
    name: ChemicalName

    @classmethod
    def from_str(cls, string: str):
        quantity, name = string.split()
        return cls(int(quantity), name)


@dataclass
class Reaction:
    quantity: int
    ins: List[ChemicalRecipe]


REACTIONS = Dict[ChemicalName, Reaction]


class Factory:
    def __init__(self, reactions: Optional[REACTIONS] = None):
        self._to_produce: DefaultDict[ChemicalName, int] = defaultdict(int)
        self._reactions = reactions if reactions else dict()
        self.ore: int = 0

    @classmethod
    def from_raw_data(cls, data: str) -> Factory:
        reactions = dict()

        for line in data.strip().split('\n'):
            ins, out = line.split(' => ')
            out = ChemicalRecipe.from_str(out)
            ins = [ChemicalRecipe.from_str(item) for item in ins.split(', ')]
            reaction = Reaction(out.quantity, ins)

            assert out.name not in reactions, f'known output {out.name}'

            reactions[out.name] = reaction

        return cls(reactions)

    def add_to_production(self, chemical: ChemicalName, quantity: int):
        self._to_produce[chemical] += quantity

    def produce(self):
        raise NotImplementedError


def solve(task: str) -> int:
    factory = Factory.from_raw_data(task)
    factory.add_to_production('FUEL', 1)
    factory.produce()
    return factory.ore
