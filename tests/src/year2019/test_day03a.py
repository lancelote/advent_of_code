"""2019 - Day 3 Part 1: Crossed Wires tests."""
import pytest

from src.year2019.day03a import Grid


@pytest.fixture
def grid():
    return Grid()


def test_grid_setup(grid):
    assert grid.current == (0, 0)
    assert len(grid.nodes) == 0
    assert len(grid.intersections) == 0


def test_basic_example(grid):
    wire1 = "R8,U5,L5,D3"
    wire2 = "U7,R6,D4,L4"

    grid.plot(wire1)
    grid.plot(wire2)

    assert len(grid.intersections) == 2
    assert (3, 3) in grid.intersections
    assert (6, 5) in grid.intersections
    assert grid.closest == 6


@pytest.mark.parametrize(
    "wires,distance",
    [
        (
            [
                "R75,D30,R83,U83,L12,D49,R71,U7,L72",
                "U62,R66,U55,R34,D71,R55,D58,R83",
            ],
            159,
        ),
        (
            [
                "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51",
                "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7",
            ],
            135,
        ),
    ],
)
def test_bigger_examples(wires, distance, grid):
    for wire in wires:
        grid.plot(wire)
    assert grid.closest == distance
