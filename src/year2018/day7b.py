"""2018 - Day 7 Part 2: The Sum of Its Parts.

As you're about to begin construction, four of the Elves offer to help. "The
sun will set soon; it'll go faster if we work together." Now, you need to
account for multiple people working on steps simultaneously. If multiple steps
are available, workers should still begin them in alphabetical order.

Each step takes 60 seconds plus an amount corresponding to its letter: A=1,
B=2, C=3, and so on. So, step A takes 60+1=61 seconds, while step Z takes
60+26=86 seconds. No time is required between steps.

To simplify things for the example, however, suppose you only have help from
one Elf (a total of two workers) and that each step takes 60 fewer seconds (so
that step A takes 1 second and step Z takes 26 seconds). Then, using the same
instructions as above, this is how each second would be spent:

    Second   Worker 1   Worker 2   Done
       0        C          .
       1        C          .
       2        C          .
       3        A          F       C
       4        B          F       CA
       5        B          F       CA
       6        D          F       CAB
       7        D          F       CAB
       8        D          F       CAB
       9        D          .       CABF
      10        E          .       CABFD
      11        E          .       CABFD
      12        E          .       CABFD
      13        E          .       CABFD
      14        E          .       CABFD
      15        .          .       CABFDE

Each row represents one second of time. The Second column identifies how many
seconds have passed as of the beginning of that second. Each worker column
shows the step that worker is currently doing (or . if they are idle). The Done
column shows completed steps.

Note that the order of the steps has changed; this is because steps now take
time to finish and multiple workers can begin multiple steps simultaneously.

In this example, it would take 15 seconds for two workers to complete these
steps.

With 5 workers and the 60+ second step durations described above, how long will
it take to complete all of the steps?
"""
from collections import defaultdict
from string import ascii_uppercase
from typing import DefaultDict
from typing import Set

from src.year2018.day7a import next_step
from src.year2018.day7a import Parents
from src.year2018.day7a import process_date
from src.year2018.day7a import Step


def solve(task: str, steps=ascii_uppercase, workers=5, duration=60) -> int:
    """Get time of work for given workers."""
    total_seconds = 0

    done: Set[Step] = set()
    todo = set(steps)

    job_step: DefaultDict[int, Step] = defaultdict(str)
    job_time: DefaultDict[int, int] = defaultdict(int)

    workers = set(range(workers))
    parents: Parents = process_date(task)

    while len(done) != len(steps):
        # Get complete jobs or update work time
        for worker in workers:
            # In progress
            if job_time[worker] != 0 and job_step[worker] != "":
                job_time[worker] -= 1

            # Done
            else:
                if job_time[worker] == 0 and job_step[worker] != "":
                    done.add(job_step[worker])
                    job_step[worker] = ""

        # Assign new jobs
        for worker in workers:
            # Ready to work
            if job_step[worker] == "":
                new_step = next_step(parents, done, todo)
                if new_step:
                    todo.remove(new_step)
                    job_step[worker] = new_step
                    job_time[worker] = duration + ord(new_step) - 65

        total_seconds += 1
    return total_seconds - 1
