"""2020 - Day 12 Part 1: Rain Risk."""

from src.year2020.day12a import Direction, Instruction, Ship


def test_basic_example():
    ship = Ship()
    ship.apply_instruction(Instruction.from_line("F10"))

    assert ship.x == 10
    assert ship.y == 0

    ship.apply_instruction(Instruction.from_line("N3"))

    assert ship.x == 10
    assert ship.y == 3

    ship.apply_instruction(Instruction.from_line("F7"))

    assert ship.x == 17
    assert ship.y == 3

    ship.apply_instruction(Instruction.from_line("R90"))

    assert ship.x == 17
    assert ship.y == 3
    assert ship.direction is Direction.SOUTH

    ship.apply_instruction(Instruction.from_line("F11"))

    assert ship.x == 17
    assert ship.y == -8
    assert ship.manhattan_distance == 25
