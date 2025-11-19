from pathlib import Path

coords_count: dict[tuple[int, int], list[tuple[int, int]]] = {}

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
            coords_count.setdefault((x, y), []).append((id, width * height))

coords_uniques = [
    candidate[0] for candidate in coords_count.values() if len(candidate) == 1
]

for id, size in set(coords_uniques):
    if len([True for candidate in coords_uniques if candidate[0] == id]) == size:
        print(id)
