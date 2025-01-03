from hashlib import md5
from pathlib import Path

door_id = Path(Path(__file__).parent, "input").read_text()

idx = 0
password = ""

for _ in range(8):
    hash = md5(f"{door_id}{idx}".encode()).hexdigest()

    while not hash.startswith("00000"):
        idx += 1
        hash = md5(f"{door_id}{idx}".encode()).hexdigest()
    idx += 1

    password += hash[5]

print(f"Result: {password}")
