"""Day 12 Part 1: Subterranean Sustainability.

The year 518 is significantly more underground than your history books implied.
Either that, or you've arrived in a vast cavern network under the North Pole.

After exploring a little, you discover a long tunnel that contains a row of
small pots as far as you can see to your left and right. A few of them contain
plants - someone is trying to grow things in these geothermally-heated caves.

The pots are numbered, with 0 in front of you. To the left, the pots are
numbered -1, -2, -3, and so on; to the right, 1, 2, 3.... Your puzzle input
contains a list of pots from 0 to the right and whether they do (#) or do not
(.) currently contain a plant, the initial state. (No other pots currently
contain plants.) For example, an initial state of #..##.... indicates that pots
0, 3, and 4 currently contain plants.

Your puzzle input also contains some notes you find on a nearby table: someone
has been trying to figure out how these plants spread to nearby pots. Based on
the notes, for each generation of plants, a given pot has or does not have a
plant based on whether that pot (and the two pots on either side of it) had a
plant in the last generation. These are written as LLCRR => N, where L are pots
to the left, C is the current pot being considered, R are the pots to the
right, and N is whether the current pot will have a plant in the next
generation. For example:

    A note like ..#.. => . means that a pot that contains a plant but with no
        plants within two pots of it will not have a plant in it during the
        next generation.
    A note like ##.## => . means that an empty pot with two plants on each side
        of it will remain empty in the next generation.
    A note like .##.# => # means that a pot has a plant in a given generation
    if, in the previous generation, there were plants in that pot, the one
    immediately to the left, and the one two pots to the right, but not in the
    ones immediately to the right and two to the left.

It's not clear what these plants are for, but you're sure it's important, so
you'd like to make sure the current configuration of plants is sustainable by
determining what will happen after 20 generations.

For example, given the following input:

    initial state: #..#.#..##......###...###

    ...## => #
    ..#.. => #
    .#... => #
    .#.#. => #
    .#.## => #
    .##.. => #
    .#### => #
    #.#.# => #
    #.### => #
    ##.#. => #
    ##.## => #
    ###.. => #
    ###.# => #
    ####. => #

For brevity, in this example, only the combinations which do produce a plant
are listed. (Your input includes all possible combinations.) Then, the next 20
generations will look like this:

                     1         2         3
           0         0         0         0
     0: ...#..#.#..##......###...###...........
     1: ...#...#....#.....#..#..#..#...........
     2: ...##..##...##....#..#..#..##..........
     3: ..#.#...#..#.#....#..#..#...#..........
     4: ...#.#..#...#.#...#..#..##..##.........
     5: ....#...##...#.#..#..#...#...#.........
     6: ....##.#.#....#...#..##..##..##........
     7: ...#..###.#...##..#...#...#...#........
     8: ...#....##.#.#.#..##..##..##..##.......
     9: ...##..#..#####....#...#...#...#.......
    10: ..#.#..#...#.##....##..##..##..##......
    11: ...#...##...#.#...#.#...#...#...#......
    12: ...##.#.#....#.#...#.#..##..##..##.....
    13: ..#..###.#....#.#...#....#...#...#.....
    14: ..#....##.#....#.#..##...##..##..##....
    15: ..##..#..#.#....#....#..#.#...#...#....
    16: .#.#..#...#.#...##...#...#.#..##..##...
    17: ..#...##...#.#.#.#...##...#....#...#...
    18: ..##.#.#....#####.#.#.#...##...##..##..
    19: .#..###.#..#.#.#######.#.#.#..#.#...#..
    20: .#....##....#####...#######....#.#..##.

The generation is shown along the left, where 0 is the initial state. The pot
numbers are shown along the top, where 0 labels the center pot,
negative-numbered pots extend to the left, and positive pots extend toward the
right. Remember, the initial state begins at pot 0, which is not the leftmost
pot used in this example.

After one generation, only seven plants remain. The one in pot 0 matched the
rule looking for ..#.., the one in pot 4 matched the rule looking for .#.#.,
pot 9 matched .##.., and so on.

In this example, after 20 generations, the pots shown as # contain plants, the
furthest left of which is pot -2, and the furthest right of which is pot 34.
Adding up all the numbers of plant-containing pots after the 20th generation
produces 325.

After 20 generations, what is the sum of the numbers of all pots which contain
a plant?
"""
from enum import Enum
from typing import Dict
from typing import Tuple


class Pot(Enum):
    """Represent a pot with (#) or without (.) a plant."""

    EMPTY = "."
    PLANT = "#"


POT_ID = int
GEN = Dict[POT_ID, Pot]
PATTERN = str
PATTERNS = Dict[PATTERN, Pot]


def process_data(task: str) -> Tuple[GEN, PATTERNS]:
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


def print_plants(generation: GEN, generation_id: int = 0):
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
