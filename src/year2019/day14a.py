"""2019 - Day 14 Part 1: Space Stoichiometry."""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from typing import Dict, List, DefaultDict


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
    def __init__(self, reactions: REACTIONS):
        self._to_produce: DefaultDict[ChemicalName, int] = defaultdict(int)
        self.reactions = reactions

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
        raise NotImplementedError

    def produce(self):
        raise NotImplementedError

    @property
    def ore(self) -> int:
        return self._to_produce['ORE']


def solve(task: str) -> int:
    factory = Factory.from_raw_data(task)
    factory.add_to_production('FUEL', 1)
    factory.produce()
    return factory.ore
