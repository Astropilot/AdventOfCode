from pathlib import Path

coords_count: dict[tuple[int, int], int] = {}

with Path(Path(__file__).parent, "input").open() as f:
    lines = [line.rstrip("\n") for line in f]

for line in lines:
    id_raw, _, coords_raw, size_raw = line.split(" ")
    x_raw, y_raw = coords_raw.split(",")
    width_raw, height_raw = size_raw.split("x")

    id = int(id_raw[1:])
    x_start = int(x_raw)
    y_start = int(y_raw[:-1])
    width = int(width_raw)
    height = int(height_raw)

    for y in range(y_start, y_start + height):
        for x in range(x_start, x_start + width):
            coords_count[(x, y)] = coords_count.get((x, y), 0) + 1

print(len([True for count in coords_count.values() if count >= 2]))
