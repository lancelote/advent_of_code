"""2019 - Day 14 Part 1: Space Stoichiometry tests."""

from textwrap import dedent

from src.year2019.day14a import ChemicalRecipe, Reaction, Factory


def test_read_task_data():
    test_data = dedent("""
        10 ORE => 10 A
        1 ORE => 1 B
        7 A, 1 B => 1 C
        7 A, 1 C => 1 D
        7 A, 1 D => 1 E
        7 A, 1 E => 1 FUEL
    """)
    expected_reactions = {
        'A': Reaction(10, [ChemicalRecipe(10, 'ORE'), ]),
        'B': Reaction(1, [ChemicalRecipe(1, 'ORE'), ]),
        'C': Reaction(1, [ChemicalRecipe(7, 'A'), ChemicalRecipe(1, 'B'), ]),
        'D': Reaction(1, [ChemicalRecipe(7, 'A'), ChemicalRecipe(1, 'C'), ]),
        'E': Reaction(1, [ChemicalRecipe(7, 'A'), ChemicalRecipe(1, 'D'), ]),
        'FUEL': Reaction(1, [ChemicalRecipe(7, 'A'), ChemicalRecipe(1, 'E'), ]),
    }

    factory = Factory.from_raw_data(test_data)

    assert factory.reactions == expected_reactions
