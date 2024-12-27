import typing as t
from pathlib import Path


class CoordsT(t.NamedTuple):
    x: int
    y: int


with Path(Path(__file__).parent, "input").open() as f:
    grid = [list(line.rstrip("\n")) for line in f]

HEIGHT = len(grid)
WIDTH = len(grid[0])

start = CoordsT(0, 0)
trees_encountered = 0

while start.y < HEIGHT:
    start = CoordsT((start.x + 3) % WIDTH, start.y + 1)

    if start.y < HEIGHT and grid[start.y][start.x] == "#":
        trees_encountered += 1

print(f"Result: {trees_encountered}")
