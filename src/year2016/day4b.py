"""2016 - Day 4 Part 2: Security Through Obscurity.

With all the decoy data out of the way, it's time to decrypt this list and get
moving.

The room names are encrypted by a state-of-the-art shift cipher, which is
nearly unbreakable without the right software. However, the information kiosk
designers at Easter Bunny HQ were not expecting to deal with a master
cryptographer like yourself.

To decrypt a room name, rotate each letter forward through the alphabet a
number of times equal to the room's sector ID. A becomes B, B becomes C, Z
becomes A, and so on. Dashes become spaces.

For example, the real name for qzmt-zixmtkozy-ivhz-343 is very encrypted name.

What is the sector ID of the room where North Pole objects are stored?
"""
from src.year2016.day4a import process_data


def shift(char: str, key: int) -> str:
    """Shift the character by the given key."""
    if char == "-":
        return " "
    else:
        return chr(97 + (ord(char) - 97 + key % 26) % 26)


def decipher(ciphered_name: str, key: int) -> str:
    """Decipher the room name."""
    return "".join(shift(char, key) for char in ciphered_name)


def solve(task: str) -> int:
    """Find the room where North Pole objects are stored."""
    rooms = process_data(task)
    for room in rooms:
        name = decipher(room.name, room.sector_id)
        if "north" in name:
            return room.sector_id
    raise ValueError("North Pole storage was not found")
