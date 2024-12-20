import operator
import typing as t
from functools import reduce
from pathlib import Path


class CoordsT(t.NamedTuple):
    x: int
    y: int


with Path(Path(__file__).parent, "input").open() as f:
    grid = [list(map(int, line.rstrip("\n"))) for line in f]

HEIGHT = len(grid)
WIDTH = len(grid[0])

low_points: set[CoordsT] = set()
walls: set[CoordsT] = set()


def get_neighbors(coords: CoordsT, walls: set[CoordsT]) -> list[CoordsT]:
    neighbors: list[CoordsT] = []

    for dx, dy in ((0, -1), (1, 0), (0, 1), (-1, 0)):
        new_coords = CoordsT(coords.x + dx, coords.y + dy)
        if (
            0 <= new_coords.x < WIDTH
            and 0 <= new_coords.y < HEIGHT
            and new_coords not in walls
        ):
            neighbors.append(new_coords)
    return neighbors


def dfs(start: CoordsT, walls: set[CoordsT], discovered: set[CoordsT]) -> None:
    discovered.add(start)

    for neighbor in get_neighbors(start, walls):
        if neighbor not in discovered:
            dfs(neighbor, walls, discovered)


for y in range(HEIGHT):
    for x in range(WIDTH):
        if grid[y][x] == 9:
            walls.add(CoordsT(x, y))
        is_low = True
        for dx, dy in ((0, -1), (1, 0), (0, 1), (-1, 0)):
            xx = x + dx
            yy = y + dy
            if 0 <= xx < WIDTH and 0 <= yy < HEIGHT and grid[yy][xx] <= grid[y][x]:
                is_low = False
                break
        if is_low:
            low_points.add(CoordsT(x, y))

basins_sizes: list[int] = []
for point in low_points:
    basin: set[CoordsT] = set()

    dfs(point, walls, basin)

    basins_sizes.append(len(basin))

largest_basins = sorted(basins_sizes, reverse=True)[:3]
result = reduce(operator.mul, largest_basins, 1)

print(f"Result: {result}")  # Result: 950600
