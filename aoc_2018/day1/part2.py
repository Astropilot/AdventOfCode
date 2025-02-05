from pathlib import Path

with Path(Path(__file__).parent, "input").open() as f:
    lines = [int(line.rstrip("\n")) for line in f]

frequency = 0
frequencies: set[int] = {0}
i = 0

while True:
    frequency += lines[i]

    if frequency in frequencies:
        break
    frequencies.add(frequency)

    i = (i + 1) % len(lines)

print(f"Result: {frequency}")
