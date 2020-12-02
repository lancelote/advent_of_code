"""2019 - Day 14 Part 1: Space Stoichiometry tests."""
from textwrap import dedent

import pytest

from src.year2019.day14a import ChemicalRecipe
from src.year2019.day14a import Factory
from src.year2019.day14a import Reaction


def test_read_task_data():
    test_data = dedent(
        """
        10 ORE => 10 A
        1 ORE => 1 B
        7 A, 1 B => 1 C
        7 A, 1 C => 1 D
        7 A, 1 D => 1 E
        7 A, 1 E => 1 FUEL
    """
    )
    expected_reactions = {
        "A": Reaction(
            10,
            [
                ChemicalRecipe(10, "ORE"),
            ],
        ),
        "B": Reaction(
            1,
            [
                ChemicalRecipe(1, "ORE"),
            ],
        ),
        "C": Reaction(
            1,
            [
                ChemicalRecipe(7, "A"),
                ChemicalRecipe(1, "B"),
            ],
        ),
        "D": Reaction(
            1,
            [
                ChemicalRecipe(7, "A"),
                ChemicalRecipe(1, "C"),
            ],
        ),
        "E": Reaction(
            1,
            [
                ChemicalRecipe(7, "A"),
                ChemicalRecipe(1, "D"),
            ],
        ),
        "FUEL": Reaction(
            1,
            [
                ChemicalRecipe(7, "A"),
                ChemicalRecipe(1, "E"),
            ],
        ),
    }

    factory = Factory.from_raw_data(test_data)

    assert factory._reactions == expected_reactions


def test_add_to_production():
    factory = Factory()

    factory.add_to_production("FOO", 1)
    factory.add_to_production("BAR", 3)
    factory.add_to_production("FOO", 1)

    assert factory._to_produce == {"FOO": 2, "BAR": 3}


@pytest.mark.xfail
@pytest.mark.parametrize(
    "data,expected",
    [
        (
            dedent(
                """
            9 ORE => 2 A
            8 ORE => 3 B
            7 ORE => 5 C
            3 A, 4 B => 1 AB
            5 B, 7 C => 1 BC
            4 C, 1 A => 1 CA
            2 AB, 3 BC, 4 CA => 1 FUEL
        """
            ),
            165,
        ),
        (
            dedent(
                """
            10 ORE => 10 A
            1 ORE => 1 B
            7 A, 1 B => 1 C
            7 A, 1 C => 1 D
            7 A, 1 D => 1 E
            7 A, 1 E => 1 FUEL
        """
            ),
            31,
        ),
    ],
)
def test_produce(data, expected):
    factory = Factory.from_raw_data(data)
    factory.add_to_production("FUEL", 1)
    factory.produce()

    assert factory.ore == expected
