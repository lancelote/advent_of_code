"""2016 - Day 4 Part 1: Security Through Obscurity.

Finally, you come across an information kiosk with a list of rooms. Of course,
the list is encrypted and full of decoy data, but the instructions to decode
the list are barely hidden nearby. Better remove the decoy data first.

Each room consists of an encrypted name (lowercase letters separated by dashes)
followed by a dash, a sector ID, and a checksum in square brackets.

A room is real (not a decoy) if the checksum is the five most common letters in
the encrypted name, in order, with ties broken by alphabetization. For example:

    - aaaaa-bbb-z-y-x-123[abxyz] is a real room because the most common letters
      are a (5), b (3), and then a tie between x, y, and z, which are listed
      alphabetically.
    - a-b-c-d-e-f-g-h-987[abcde] is a real room because although the letters
      are all tied (1 of each), the first five are listed alphabetically.
    - not-a-real-room-404[oarel] is a real room.
    - totally-real-room-200[decoy] is not.

Of the real rooms from the list above, the sum of their sector IDs is 1514.

What is the sum of the sector IDs of the real rooms?
"""

import operator
import re
from collections import namedtuple, Counter
from typing import List

Room = namedtuple('Room', 'name sector_id checksum')
ROOM_PATTERN = re.compile(
    r'^(?P<name>[a-z-]+)-(?P<sector_id>\d+)\[(?P<checksum>[a-z]+)\]$')


def process_data(data: str) -> List[Room]:
    """Convert raw data into the list of rooms."""
    rooms = []
    lines = data.strip().split()
    for line in lines:
        match = re.search(ROOM_PATTERN, line)
        name = match.group('name')
        sector_id = int(match.group('sector_id'))
        checksum = match.group('checksum')
        room = Room(name, sector_id, checksum)
        rooms.append(room)
    return rooms


def is_real(room: Room) -> bool:
    """Check if the room is real."""
    common_5 = Counter(room.name.replace('-', '')).most_common()
    common_5.sort(key=operator.itemgetter(0))  # Sort alphabetically
    common_5.sort(key=operator.itemgetter(1), reverse=True)  # Sort by number
    return ''.join(char for char, _ in common_5[:5]) == room.checksum


def solve(task: str) -> int:
    """Calculate id sum of real rooms."""
    id_sum = 0
    rooms = process_data(task)
    for room in rooms:
        if is_real(room):
            id_sum += room.sector_id
    return id_sum
