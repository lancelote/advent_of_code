"""2018 - Day 7 Part 2: The Sum of Its Parts."""

from collections import defaultdict
from string import ascii_uppercase
from typing import DefaultDict

from src.year2018.day07a import Parents
from src.year2018.day07a import Step
from src.year2018.day07a import next_step
from src.year2018.day07a import process_date


def solve(
    task: str,
    steps: str = ascii_uppercase,
    n_workers: int = 5,
    duration: int = 60,
) -> int:
    """Get time of work for given workers."""
    total_seconds = 0

    done: set[Step] = set()
    todo = set(steps)

    job_step: DefaultDict[int, Step] = defaultdict(str)
    job_time: DefaultDict[int, int] = defaultdict(int)

    workers = set(range(n_workers))
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
