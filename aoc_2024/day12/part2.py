import typing as t
from pathlib import Path

with Path(Path(__file__).parent, "input").open() as f:
    grid = [list(line.rstrip("\n")) for line in f]


class Plant(t.NamedTuple):
    x: int
    y: int
    plant: str


height = len(grid)
width = len(grid[0])
plants: list[Plant] = []

for y in range(len(grid)):
    for x in range(len(grid[y])):
        plants.append(Plant(x, y, grid[y][x]))

regions: list[set[Plant]] = []


def find_region(start: Plant, region: set[Plant], discovered: set[Plant]) -> None:
    region.add(start)
    discovered.add(start)

    for dx, dy in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
        if (0 <= start.x + dx < width and 0 <= start.y + dy < height) and grid[
            start.y + dy
        ][start.x + dx] == start.plant:
            neighbor = Plant(start.x + dx, start.y + dy, start.plant)
            if neighbor not in discovered:
                find_region(neighbor, region, discovered)


discovered: set[Plant] = set()
for plant in plants:
    region: set[Plant] = set()

    if plant in discovered:
        continue

    find_region(plant, region, discovered)

    if len(region) > 0:
        regions.append(region)

total_price = 0
for region in regions:
    area = len(region)
    sides = 0

    faces_x: dict[tuple[int, t.Literal["left", "right"]], set[int]] = {}
    faces_y: dict[tuple[int, t.Literal["up", "down"]], set[int]] = {}

    for plant in region:
        if Plant(plant.x, plant.y - 1, plant.plant) not in region:
            faces_y.setdefault((plant.y, "up"), set()).add(plant.x)
        if Plant(plant.x, plant.y + 1, plant.plant) not in region:
            faces_y.setdefault((plant.y, "down"), set()).add(plant.x)
        if Plant(plant.x - 1, plant.y, plant.plant) not in region:
            faces_x.setdefault((plant.x, "left"), set()).add(plant.y)
        if Plant(plant.x + 1, plant.y, plant.plant) not in region:
            faces_x.setdefault((plant.x, "right"), set()).add(plant.y)

    for x_dir in faces_x:
        last_y_coords = None
        for y in sorted(faces_x[x_dir]):
            if last_y_coords is None or y != last_y_coords + 1:
                sides += 1
            last_y_coords = y
    for y_dir in faces_y:
        last_x_coords = None
        for x in sorted(faces_y[y_dir]):
            if last_x_coords is None or x != last_x_coords + 1:
                sides += 1
            last_x_coords = x

    total_price += area * sides

print(f"Result: {total_price}")
