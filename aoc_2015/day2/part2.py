from pathlib import Path

with Path(Path(__file__).parent, "input").open() as f:
    dimensions = [line.rstrip("\n") for line in f]

total = 0
for dimension in dimensions:
    l, w, h = map(int, dimension.split("x"))

    perimeters = [2 * l + 2 * w, 2 * l + 2 * h, 2 * w + 2 * h]
    total += min(perimeters) + (l * w * h)

print(f"Result: {total}")
