"""2018 - Day 9 Part 1: Marble Mania tests."""

import pytest

from src.year2018.day9a import parse_task, solve, Marble


def test_parse_task():
    sample_task = '411 players; last marble is worth 71058 points'
    assert parse_task(sample_task) == (411, 71058)


class TestMarble:

    @staticmethod
    def generate_circle(step):
        """Generate a marble circle returning it's start and end."""
        start = current = Marble.get_zero_marble()
        for i in range(1, step + 1):
            new = Marble(i)
            current.insert_new(new)
            current = new
        return start, current

    @staticmethod
    def get_circle_values(start):
        """Generate a list of values for each marble in circle."""
        sequence = [0]
        start = start.child

        while start.value != 0:
            sequence.append(start.value)
            start = start.child
        return sequence

    def test_get_zero_marble(self):
        marble = Marble.get_zero_marble()
        assert marble.value == 0
        assert marble.child == marble
        assert marble.parent == marble

    @pytest.mark.parametrize(
        ('step', 'expected_sequence'),
        [
            (2, [0, 2, 1]),
            (9, [0, 8, 4, 9, 2, 5, 1, 6, 3, 7])
        ]
    )
    def test_insert_new(self, step, expected_sequence):
        start, _ = self.generate_circle(step)
        assert self.get_circle_values(start) == expected_sequence

    def test_remove_counter_clockwise(self):
        start, end = self.generate_circle(5)
        current, value = end.remove_counter_clockwise(2)
        assert value == 4
        assert current.value == 2
        assert self.get_circle_values(start) == [0, 2, 5, 1, 3]


@pytest.mark.parametrize(
    ('task', 'expected_score'),
    [
        ('9 players; last marble is worth 25 points', 32),
        ('10 players; last marble is worth 1618 points', 8317),
        ('13 players; last marble is worth 7999 points', 146373),
        ('17 players; last marble is worth 1104 points', 2764),
        ('21 players; last marble is worth 6111 points', 54718),
        ('30 players; last marble is worth 5807 points', 37305),
    ]
)
def test_solve(task, expected_score):
    assert solve(task) == expected_score
