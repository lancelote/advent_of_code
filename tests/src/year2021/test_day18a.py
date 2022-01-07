"""2021 - Day 18 Part 1: Snailfish."""
import functools
from textwrap import dedent

import pytest

from src.year2021.day18a import explode
from src.year2021.day18a import Node
from src.year2021.day18a import reduce
from src.year2021.day18a import solve
from src.year2021.day18a import split


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


@pytest.mark.parametrize(
    "from_line,to_line",
    [
        (
            "[10,1]",
            "[[5,5],1]",
        ),
        (
            "[[[[0,7],4],[15,[0,13]]],[1,1]]",
            "[[[[0,7],4],[[7,8],[0,13]]],[1,1]]",
        ),
        (
            "[[[[0,7],4],[[7,8],[0,13]]],[1,1]]",
            "[[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]",
        ),
    ],
)
def test_split(from_line, to_line):
    num = Node.from_line(from_line)
    assert str(split(num)) == to_line


@pytest.mark.parametrize(
    "from_line,to_line",
    [
        (
            "[[[[[9,8],1],2],3],4]",
            "[[[[0,9],2],3],4]",
        ),
        (
            "[7,[6,[5,[4,[3,2]]]]]",
            "[7,[6,[5,[7,0]]]]",
        ),
        (
            "[[6,[5,[4,[3,2]]]],1]",
            "[[6,[5,[7,0]]],3]",
        ),
        (
            "[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]",
            "[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]",
        ),
        (
            "[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]",
            "[[3,[2,[8,0]]],[9,[5,[7,0]]]]",
        ),
    ],
)
def test_explode(from_line, to_line):
    num = Node.from_line(from_line)
    assert str(explode(num)) == to_line


def test_reduce():
    line = "[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]"
    expected = "[[[[0,7],4],[[7,8],[6,0]]],[8,1]]"
    assert str(reduce(Node.from_line(line))) == expected


def test_sum():
    task = """
        [[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]
        [7,[[[3,7],[4,3]],[[6,3],[8,8]]]]
        [[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]
        [[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]
        [7,[5,[[3,8],[1,4]]]]
        [[2,[2,2]],[8,[8,1]]]
        [2,9]
        [1,[[[9,3],9],[[9,0],[0,7]]]]
        [[[5,[7,4]],7],1]
        [[[[4,2],2],6],[8,7]]
    """
    nums = [Node.from_line(line) for line in dedent(task).strip().splitlines()]
    expected = "[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]"
    assert str(functools.reduce(lambda x, y: x + y, nums)) == expected


def test_solve():
    task = """
        [[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
        [[[5,[2,8]],4],[5,[[9,9],0]]]
        [6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
        [[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
        [[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
        [[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
        [[[[5,4],[7,7]],8],[[8,3],8]]
        [[9,3],[[9,9],[6,[4,9]]]]
        [[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
        [[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]
    """
    assert solve(dedent(task).strip()) == 4140
