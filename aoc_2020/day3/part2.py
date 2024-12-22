import math
import typing as t
from pathlib import Path


class CoordsT(t.NamedTuple):
    x: int
    y: int


with Path(Path(__file__).parent, "input").open() as f:
    grid = [list(line.rstrip("\n")) for line in f]

HEIGHT = len(grid)
WIDTH = len(grid[0])

slopes_directions = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
slopes_positions = [
    CoordsT(0, 0),
    CoordsT(0, 0),
    CoordsT(0, 0),
    CoordsT(0, 0),
    CoordsT(0, 0),
]
trees_encountered = [0, 0, 0, 0, 0]

while any(pos.y < HEIGHT for pos in slopes_positions):
    for i_slopes, slope_pos in enumerate(slopes_positions):
        if slope_pos.y >= HEIGHT:
            continue

        slope_pos = CoordsT(
            (slope_pos.x + slopes_directions[i_slopes][0]) % WIDTH,
            slope_pos.y + slopes_directions[i_slopes][1],
        )
        slopes_positions[i_slopes] = slope_pos

        if slope_pos.y < HEIGHT and grid[slope_pos.y][slope_pos.x] == "#":
            trees_encountered[i_slopes] += 1


print(f"Result: {math.prod(trees_encountered)}")  # Result: 3093068400
