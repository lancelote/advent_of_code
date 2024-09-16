"""2023 - Day 5 Part 2: If You Give A Seed A Fertilizer"""

from typing import TypeAlias

Seed: TypeAlias = tuple[int, int]
Range: TypeAlias = tuple[int, int, int]
Block: TypeAlias = list[Range]


def process_data(task: str) -> tuple[list[Seed], list[Block]]:
    seeds: list[Seed] = []
    blocks: list[Block] = []

    first_line, *rest = task.split("\n\n")
    seed_ints = [int(x) for x in first_line.split(": ")[1].split()]

    for i in range(0, len(seed_ints), 2):
        seeds.append((seed_ints[i], seed_ints[i] + seed_ints[i + 1]))

    for paragraph in rest:
        block: Block = []

        _, *lines = paragraph.split("\n")

        for line in lines:
            dst, src, length = (int(x) for x in line.split(" "))
            block.append((dst, src, length))

        blocks.append(block)

    return seeds, blocks


def solve(task: str) -> int:
    seeds, blocks = process_data(task)

    for block in blocks:
        new_seeds: list[Seed] = []

        while seeds:
            start, end = seeds.pop()

            for dst, src, length in block:
                diff = dst - src

                # |-----|  range
                #   |-|    seed
                if start >= src and end <= src + length:
                    new_seeds.append((start + diff, end + diff))
                    break

                #   |---|  range
                # |---|    seed
                elif start < src < end <= src + length:
                    seeds.append((start, src))
                    new_seeds.append((src + diff, end + diff))
                    break

                # |---|    range
                #   |---|  seed
                elif src <= start < src + length <= end:
                    new_seeds.append((start + diff, src + length + diff))
                    seeds.append((src + length, end))
                    break

                #   |-|    range
                # |-----|  seed
                elif start <= src and end >= src + length:
                    new_seeds.append((src + diff, src + length + diff))
                    seeds.append((start, src))
                    seeds.append((src + length, end))
                    break
            else:
                new_seeds.append((start, end))

        seeds = new_seeds

    return min(start for start, _ in seeds)
