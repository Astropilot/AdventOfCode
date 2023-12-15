from pathlib import Path

contents = Path(Path(__file__).parent, "input").read_text()
contents = contents.strip("\n")


def hash_algo(s: str) -> int:
    current = 0

    for c in s:
        current += ord(c)
        current *= 17
        current = current % 256

    return current


sum_hash = 0
for step in contents.split(","):
    sum_hash += hash_algo(step)

print(f"Result: {sum_hash}")  # Result: 517015
