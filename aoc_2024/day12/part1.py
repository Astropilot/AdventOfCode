from pathlib import Path
from typing import NamedTuple

with Path(Path(__file__).parent, "input").open() as f:
    grid = [list(line.rstrip("\n")) for line in f]


class Plant(NamedTuple):
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
    perimeter = 0

    for plant in region:
        for dx, dy in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
            if Plant(plant.x + dx, plant.y + dy, plant.plant) not in region:
                perimeter += 1

    total_price += area * perimeter

print(f"Result: {total_price}")
