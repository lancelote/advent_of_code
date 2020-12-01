"""2019 - Day 6 Part 2: Universal Orbit Map tests."""

import pytest

from src.year2019.day6b import closest_distance, process_data


@pytest.fixture
def raw_orbit_data():
    return (
        "COM)B\nB)C\nC)D\nD)E\nE)F\nB)G\n"
        "G)H\nD)I\nE)J\nJ)K\nK)L\nK)YOU\nI)SAN"
    )


def test_process_data(raw_orbit_data):
    orbit_map = process_data(raw_orbit_data)

    assert len(orbit_map) == 14
    assert orbit_map["D"] == {"C", "E", "I"}


def test_closest_distance(raw_orbit_data):
    orbit_map = process_data(raw_orbit_data)

    assert closest_distance("YOU", "SAN", orbit_map) == 4
