"""2019 - Day 6 Part 1: Universal Orbit Map tests."""

import pytest

from src.year2019.day6a import process_data


@pytest.fixture
def raw_orbit_data():
    return 'COM)B\nB)C\nC)D\nD)E\nE)F\nB)G\nG)H\nD)I\nE)J\nJ)K\nK)L'


def test_process_data(raw_orbit_data):
    orbit_map = process_data(raw_orbit_data)

    assert len(orbit_map) == 12
    assert len(orbit_map['COM'].satellites) == 1
    assert len(orbit_map['B'].satellites) == 2
    assert len(orbit_map['F'].satellites) == 0


def test_traverse(raw_orbit_data):
    orbit_map = process_data(raw_orbit_data)

    assert orbit_map['COM'].traverse() == 42
