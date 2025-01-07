from pathlib import Path

with Path(Path(__file__).parent, "input").open() as f:
    masses = [int(line.rstrip("\n")) for line in f]

total_mass = 0

for mass in masses:
    mass = (mass // 3) - 2
    total_mass += mass

    while True:
        mass = (mass // 3) - 2

        if mass <= 0:
            break
        total_mass += mass


print(f"Result: {total_mass}")
