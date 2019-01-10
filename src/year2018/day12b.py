"""Day 12 Part 2: Subterranean Sustainability.

You realize that 20 generations aren't enough. After all, these plants will
need to last another 1500 years to even reach your timeline, not to mention
your future.

After fifty billion (50000000000) generations, what is the sum of the numbers
of all pots which contain a plant?
"""

from typing import Dict


STATE = Dict[int, str]
PATTERN = str
PATTERNS = Dict[PATTERN, str]


class Farm:

    def __init__(self, state: STATE, patterns: PATTERNS):
        self.state = state
        self.patterns = patterns

    @classmethod
    def from_task(cls, task: str) -> 'Farm':
        lines = task.strip().split('\n')
        raw_state = lines[0].split()[2]
        state = dict(enumerate(raw_state))
        patterns = {line[:5]: line[9] for line in lines[2:]}
        return cls(state, patterns)


def solve(task: str) -> int:
    farm = Farm.from_task(task)
