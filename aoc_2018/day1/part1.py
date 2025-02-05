from pathlib import Path

with Path(Path(__file__).parent, "input").open() as f:
    lines = [int(line.rstrip("\n")) for line in f]

result = sum(lines)

print(f"Result: {result}")
