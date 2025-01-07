from pathlib import Path

with Path(Path(__file__).parent, "input").open() as f:
    masses = [int(line.rstrip("\n")) for line in f]

total_mass = 0

for mass in masses:
    total_mass += (mass // 3) - 2

print(f"Result: {total_mass}")
