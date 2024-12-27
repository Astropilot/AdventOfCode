from pathlib import Path

with Path(Path(__file__).parent, "input").open() as f:
    dimensions = [line.rstrip("\n") for line in f]

total = 0
for dimension in dimensions:
    l, w, h = map(int, dimension.split("x"))

    sides = [l * w, w * h, h * l]
    total += (2 * sides[0] + 2 * sides[1] + 2 * sides[2]) + min(sides)

print(f"Result: {total}")
