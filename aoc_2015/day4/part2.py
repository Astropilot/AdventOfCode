from hashlib import md5
from pathlib import Path

key = Path(Path(__file__).parent, "input").read_text()

i = 0
while True:
    secret = key + str(i)
    if md5(secret.encode()).hexdigest().startswith("000000"):
        break

    i += 1

print(f"Result: {i}")
