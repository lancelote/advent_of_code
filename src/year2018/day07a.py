r"""2018 - Day 7 Part 1: The Sum of Its Parts."""

from collections import defaultdict
from collections.abc import Generator
from string import ascii_uppercase
from typing import DefaultDict

Step = str
Parents = DefaultDict[Step, set[Step]]
StepGenerator = Generator[Step, None, None]


def process_date(data: str) -> Parents:
    """Generate a dict of step: parents from raw data."""
    parents: Parents = defaultdict(set)

    for line in data.strip().split("\n"):
        parent, child = line[5], line[36]
        parents[child].add(parent)

    return parents


def next_step(
    parents: Parents, done: set[Step], todo: set[Step]
) -> Step | None:
    """Get next available step to take."""
    ready = set()
    for step in todo:
        if parents[step].issubset(done):
            ready.add(step)
    return min(ready) if ready else None


def ordered_steps(parents: Parents, steps: str) -> StepGenerator:
    """Yield next available step in the correct order."""
    done: set[Step] = set()
    todo: set[Step] = set(steps)

    while todo:
        new_step = next_step(parents, done, todo)
        if new_step:
            yield new_step
            done.add(new_step)
            todo.remove(new_step)


def solve(task: str, steps: str = ascii_uppercase) -> str:
    """Find the sequence of steps."""
    parents = process_date(task)
    return "".join(ordered_steps(parents, steps))
