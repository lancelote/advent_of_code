"""2019 - Day 12 Part 1: The N-Body Problem tests."""

from textwrap import dedent

import pytest
from src.year2019.day12a import Moon, process_data


@pytest.fixture
def sample_data():
    return dedent("""
        <x=1, y=3, z=-11>
        <x=17, y=-10, z=-8>
        <x=-1, y=-15, z=2>
        <x=12, y=-4, z=-4>
    """)


@pytest.mark.parametrize('string,expected_moon', [
    ('<x=1, y=3, z=-11>', Moon(1, 3, -11)),
    ('<x=17, y=-10, z=-8>', Moon(17, -10, -8)),
    ('<x=-1, y=-15, z=2>', Moon(-1, -15, 2)),
    ('<x=12, y=-4, z=-4>', Moon(12, -4, -4)),
])
def test_moon_from_string(string, expected_moon):
    assert Moon.from_string(string) == expected_moon


def test_process_data(sample_data):
    assert process_data(sample_data) == (
        Moon(1, 3, -11),
        Moon(17, -10, -8),
        Moon(-1, -15, 2),
        Moon(12, -4, -4),
    )
