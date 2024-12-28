from pathlib import Path

with Path(Path(__file__).parent, "input").open() as f:
    rows = [line.rstrip("\n") for line in f]

checksum = 0

for row in rows:
    numbers = [int(n) for n in row.split("\t")]

    checksum += max(numbers) - min(numbers)

print(f"Result: {checksum}")
