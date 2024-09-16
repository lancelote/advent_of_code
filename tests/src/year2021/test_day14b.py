"""2021 - Day 14 Part 2: Extended Polymerization."""

from textwrap import dedent

from src.year2021.day14b import solve


def test_solve():
    task = dedent(
        """
        NNCB

        CH -> B
        HH -> N
        CB -> H
        NH -> C
        HB -> C
        HC -> B
        HN -> C
        NN -> C
        BH -> H
        NC -> B
        NB -> B
        BN -> B
        BB -> N
        BC -> B
        CC -> N
        CN -> C
        """
    ).strip()
    assert solve(task) == 2188189693529
