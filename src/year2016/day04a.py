"""2016 - Day 4 Part 1: Security Through Obscurity."""
import operator
import re
from collections import Counter
from typing import Any
from typing import NamedTuple

ROOM_PATTERN = re.compile(
    r"^(?P<name>[a-z-]+)-(?P<sector_id>\d+)\[(?P<checksum>[a-z]+)]$"
)


class Room(NamedTuple):
    name: str
    sector_id: int
    checksum: str


def process_data(data: str) -> list[Room]:
    """Convert raw data into the list of rooms."""
    rooms = []
    lines = data.strip().split()
    for line in lines:
        match = re.search(ROOM_PATTERN, line)
        if not match:
            raise ValueError("Wrong room line format")
        name = match.group("name")
        sector_id = int(match.group("sector_id"))
        checksum = match.group("checksum")
        room = Room(name, sector_id, checksum)
        rooms.append(room)
    return rooms


def is_real(room: Room) -> bool:
    """Check if the room is real."""
    common_5: list[tuple[Any, int]] = Counter(
        room.name.replace("-", "")
    ).most_common()
    common_5.sort(key=operator.itemgetter(0))  # Sort alphabetically
    common_5.sort(key=operator.itemgetter(1), reverse=True)  # Sort by number
    return "".join(char for char, _ in common_5[:5]) == room.checksum


def solve(task: str) -> int:
    """Calculate id sum of real rooms."""
    id_sum = 0
    rooms = process_data(task)
    for room in rooms:
        if is_real(room):
            id_sum += room.sector_id
    return id_sum
