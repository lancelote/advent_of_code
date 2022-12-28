"""2016 - Day 5 Part 2: How About a Nice Game of Chess."""
import hashlib


def print_password(password: list[str]) -> None:
    """Print current password decipher progress."""
    line = " ".join(char if char != "" else "x" for char in password)
    print("Hacking... ", line, end="\r")


def solve(task: str) -> str:
    """Find the secret door password."""
    i = 0
    password = [""] * 8
    print_password(password)

    while "" in password:
        next_try = task + str(i)
        hex_hash = hashlib.md5(next_try.encode("utf-8")).hexdigest()
        position_char = hex_hash[5]
        new_char = hex_hash[6]

        try:
            position = int(position_char)

            if hex_hash.startswith("00000") and password[position] == "":
                password[position] = new_char
                print_password(password)
        except (ValueError, IndexError):
            pass
        i += 1
    print()
    return "".join(password)
