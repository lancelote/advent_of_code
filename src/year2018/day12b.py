"""Day 12 Part 2: Subterranean Sustainability.

You realize that 20 generations aren't enough. After all, these plants will
need to last another 1500 years to even reach your timeline, not to mention
your future.

After fifty billion (50000000000) generations, what is the sum of the numbers
of all pots which contain a plant?
"""
from collections import deque

from src.year2018.day12a import get_new_generation
from src.year2018.day12a import process_data


def solve(task: str) -> int:
    """Find the sum of all pots id with plants after 50 billion generations."""
    stable_diff = 0
    generations = 50_000_000_000
    generation, patterns = process_data(task)
    prev_sum = sum(generation.keys())
    prev_diffs = deque([0, 1, 2])

    while generations:
        new_generation = get_new_generation(generation, patterns)
        new_sum = sum(new_generation.keys())
        new_diff = new_sum - prev_sum
        prev_diffs.popleft()
        prev_diffs.append(new_diff)
        if len(set(prev_diffs)) == 1:
            stable_diff = new_diff
            print(f"stable diff: {stable_diff}")
            print(f"generation: {generations}")
            break

        prev_sum = new_sum
        generation = new_generation
        generations -= 1

    return prev_sum + generations * stable_diff
