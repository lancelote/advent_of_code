"""2016 - Day 4 Part 2: Security Through Obscurity."""

from src.year2016.day04a import process_data


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
