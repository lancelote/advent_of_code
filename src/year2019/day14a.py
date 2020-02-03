"""2019 - Day 14 Part 1: Space Stoichiometry."""

from dataclasses import dataclass
from typing import Dict, List


@dataclass
class Chemical:
    quantity: int
    name: str

    @classmethod
    def from_str(cls, string: str):
        quantity, name = string.split()
        return cls(int(quantity), name)


@dataclass
class Reaction:
    quantity: int
    ins: List[Chemical]


REACTIONS = Dict[str, Reaction]


def process_data(data: str) -> REACTIONS:
    reactions = dict()

    for line in data.strip().split('\n'):
        ins, out = line.split(' => ')
        out = Chemical.from_str(out)
        ins = [Chemical.from_str(item) for item in ins.split(', ')]
        reaction = Reaction(out.quantity, ins)

        assert out.name not in reactions, f'known output {out.name}'

        reactions[out.name] = reaction

    return reactions


def get_multiplier(target: int, reaction: int) -> int:
    if target / reaction < 0:
        return 1
    elif target % reaction != 0:
        return target // reaction + 1
    else:
        return target // reaction


def count_required_ore(fuel: int, reactions: REACTIONS) -> int:
    required_ore = 0
    to_produce = [Chemical(fuel, 'FUEL')]

    while to_produce:
        target = to_produce.pop()
        reaction = reactions[target.name]
        multiplier = get_multiplier(target.quantity, reaction.quantity)
        # ToDo: update "to_produce"

    return required_ore


def solve(task: str) -> int:
    reactions = process_data(task)
    return count_required_ore(1, reactions)
