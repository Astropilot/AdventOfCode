from pathlib import Path

contents = Path(Path(__file__).parent, "input").read_text()

crabs = list(map(int, contents.split(",")))

fuel_per_position: dict[int, int] = {}

for crab_position in range(0, max(crabs)):
    if crab_position in fuel_per_position:
        continue
    fuel_needed = 0
    for crab in crabs:
        n = abs(crab_position - crab)
        fuel_needed += (n * (n + 1)) // 2
    fuel_per_position[crab_position] = fuel_needed


result = min(fuel_per_position.values())
print(f"Result: {result}")
