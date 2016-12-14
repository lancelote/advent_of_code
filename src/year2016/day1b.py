"""
--- Part Two ---

Then, you notice the instructions continue on the back of the Recruiting
Document. Easter Bunny HQ is actually at the first location you visit twice.

For example, if your instructions are R8, R4, R4, R8, the first location you
visit twice is 4 blocks away, due East.

How many blocks away is the first location you visit twice?
"""
from src.year2016.day1a import processed_data, update_direction, \
    update_coordinates, calculate_distance


def solve(task: str) -> int:
    """How many blocks away is Easter Bunny HQ?"""
    direction = 0  # North
    bunny_hq = (0, 0)
    visited = [bunny_hq]

    instructions = processed_data(task)

    for instruction in instructions:
        direction = update_direction(direction, instruction.direction)
        bunny_hq = update_coordinates(bunny_hq, direction, instruction.distance)

        # ToDo: Rewrite the logic for visited check
        if bunny_hq in visited:
            break
        else:
            visited.append(bunny_hq)

    return calculate_distance(bunny_hq)
