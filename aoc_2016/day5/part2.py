from hashlib import md5
from pathlib import Path

door_id = Path(Path(__file__).parent, "input").read_text()

idx = 0
password = list("ZZZZZZZZ")

while "Z" in password:
    hash = md5(f"{door_id}{idx}".encode()).hexdigest()
    idx += 1

    if not hash.startswith("00000"):
        continue

    position = int(hash[5], 16)

    if (not (0 <= position <= 7)) or password[position] != "Z":
        continue

    password[position] = hash[6]


print(f"Result: {"".join(password)}")
