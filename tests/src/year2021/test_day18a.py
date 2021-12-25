"""2021 - Day 18 Part 1: Snailfish."""
import pytest

from src.year2021.day18a import Branch
from src.year2021.day18a import Leaf
from src.year2021.day18a import Node
from src.year2021.day18a import tokenize


@pytest.mark.parametrize(
    "line,expected_tokens",
    [("[1,2]", ["[", "1", "2"]), ("[[1,22],3]", ["[", "[", "1", "22", "3"])],
)
def test_tokenize(line, expected_tokens):
    assert list(tokenize(line)) == expected_tokens


def test_from_line_1():
    root = Node.from_line("[1,2]")

    assert isinstance(root, Branch)
    assert isinstance(root.left, Leaf)
    assert root.left.value == 1

    assert isinstance(root.right, Leaf)
    assert root.right.value == 2


def test_from_line_2():
    root = Node.from_line("[9,[8,7]]")

    assert isinstance(root, Branch)
    assert isinstance(root.left, Leaf)
    assert root.left.value == 9

    assert isinstance(root.right, Branch)
    assert isinstance(root.right.left, Leaf)
    assert root.right.left.value == 8

    assert isinstance(root.right.right, Leaf)
    assert root.right.right.value == 7


@pytest.mark.parametrize(
    "line,expected_magnitude",
    [
        ("[9,1]", 29),
        ("[1,9]", 21),
        ("[[9,1],[1,9]]", 129),
        ("[[1,2],[[3,4],5]]", 143),
        ("[[[[0,7],4],[[7,8],[6,0]]],[8,1]]", 1384),
        ("[[[[1,1],[2,2]],[3,3]],[4,4]]", 445),
        ("[[[[3,0],[5,3]],[4,4]],[5,5]]", 791),
        ("[[[[5,0],[7,4]],[5,5]],[6,6]]", 1137),
        ("[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]", 3488),
    ],
)
def test_magnitude(line, expected_magnitude):
    assert Node.from_line(line).magnitude == expected_magnitude


@pytest.mark.parametrize(
    "line",
    [
        "[9,1]",
        "[[9,1],[1,9]]",
        "[[1,2],[[3,4],5]]",
    ],
)
def test_str(line):
    assert str(Node.from_line(line)) == line


def test_add():
    a = Node.from_line("[1,2]")
    b = Node.from_line("[[3,4],5]")
    c = a + b
    assert str(c) == "[[1,2],[[3,4],5]]"
