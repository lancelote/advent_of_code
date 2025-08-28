"""2019 - Day 12 Part 1: The N-Body Problem tests."""

from textwrap import dedent

import pytest

from src.year2019.day12a import Moon, System


@pytest.fixture
def sample_data():
    return dedent(
        """
        <x=1, y=3, z=-11>
        <x=17, y=-10, z=-8>
        <x=-1, y=-15, z=2>
        <x=12, y=-4, z=-4>
    """
    )


@pytest.mark.parametrize(
    "string,expected_moon",
    [
        ("<x=1, y=3, z=-11>", Moon(1, 3, -11)),
        ("<x=17, y=-10, z=-8>", Moon(17, -10, -8)),
        ("<x=-1, y=-15, z=2>", Moon(-1, -15, 2)),
        ("<x=12, y=-4, z=-4>", Moon(12, -4, -4)),
    ],
)
def test_moon_from_string(string, expected_moon):
    assert Moon.from_string(string) == expected_moon


def test_process_data(sample_data):
    assert System.from_raw_data(sample_data).moons == [
        Moon(1, 3, -11),
        Moon(17, -10, -8),
        Moon(-1, -15, 2),
        Moon(12, -4, -4),
    ]


def test_apply_moon_velocity():
    moon = Moon(x=1, y=2, z=3, dx=-2, dy=0, dz=3)

    moon.apply_velocity()

    assert moon.x == -1
    assert moon.y == 2
    assert moon.z == 6


def test_apply_gravity():
    moon1 = Moon(-1, 0, 9)
    moon2 = Moon(1, 0, 3)
    system = System([moon1, moon2])

    system.apply_gravity()

    assert moon1.dx == +1
    assert moon1.dy == 0
    assert moon1.dz == -1
    assert moon2.dx == -1
    assert moon2.dy == 0
    assert moon2.dz == +1


def test_system_two_steps():
    moon1 = Moon(-1, 0, 2)
    moon2 = Moon(2, -10, -7)
    moon3 = Moon(4, -8, 8)
    moon4 = Moon(3, 5, -1)
    system = System([moon1, moon2, moon3, moon4])

    system.step()

    assert moon1.coordinates == (2, -1, 1)
    assert moon1.velocity == (3, -1, -1)

    assert moon2.coordinates == (3, -7, -4)
    assert moon2.velocity == (1, 3, 3)

    assert moon3.coordinates == (1, -7, 5)
    assert moon3.velocity == (-3, 1, -3)

    assert moon4.coordinates == (2, 2, 0)
    assert moon4.velocity == (-1, -3, 1)

    system.step()

    assert moon1.coordinates == (5, -3, -1)
    assert moon1.velocity == (3, -2, -2)

    assert moon2.coordinates == (1, -2, 2)
    assert moon2.velocity == (-2, 5, 6)

    assert moon3.coordinates == (1, -4, -1)
    assert moon3.velocity == (0, 3, -6)

    assert moon4.coordinates == (1, -4, 2)
    assert moon4.velocity == (-1, -6, 2)


def test_moon_energy():
    moon = Moon(x=2, y=1, z=-3, dx=-3, dy=-2, dz=1)

    assert moon.potential_energy == 6
    assert moon.kinetic_energy == 6
    assert moon.energy == 36


def test_system_energy():
    system = System(
        [
            Moon(2, 1, -3, -3, -2, 1),
            Moon(1, -8, 0, -1, 1, 3),
            Moon(3, -6, 1, 3, 2, -3),
            Moon(2, 0, 4, 1, -1, -1),
        ]
    )

    assert system.potential_energy == 31
    assert system.kinetic_energy == 22
    assert system.energy == 179
