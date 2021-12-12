"""2017 - Day 6 Part 1: Memory Reallocation tests."""
from src.year2017.day06a import Memory
from src.year2017.day06a import solve


class TestMemory:
    def test_copy(self):
        assert str(Memory([1, 2, 3])) == "1 2 3"

    def test_copy_multiple_digit_numbers(self):
        assert str(Memory([11, 22, 33])) == "11 22 33"

    def test_copy_negative_numbers(self):
        assert str(Memory([-1, -11, 111])) == "-1 -11 111"

    def test_redistribute(self):
        memory = Memory([0, 2, 7, 0])
        memory.redistribute()
        assert memory.banks == [2, 4, 1, 2]
        memory.redistribute()
        assert memory.banks == [3, 1, 2, 3]
        memory.redistribute()
        assert memory.banks == [0, 2, 3, 4]
        memory.redistribute()
        assert memory.banks == [1, 3, 4, 1]
        memory.redistribute()
        assert memory.banks == [2, 4, 1, 2]


def test_solve():
    assert solve("0	2	7	0") == 5
