from pathlib import Path

with Path(Path(__file__).parent, "input").open() as f:
    grid = [list(line.rstrip("\n")) for line in f]

HEIGHT = len(grid)
WIDTH = len(grid[0])


def nearby_neighbors(x: int, y: int, grid: list[list[str]]) -> list[tuple[int, int]]:
    neighbors: list[tuple[int, int]] = []

    # Right
    for dx in range(x + 1, WIDTH):
        if grid[y][dx] != ".":
            neighbors.append((dx, y))
            break
    # Left
    for dx in range(x - 1, -1, -1):
        if grid[y][dx] != ".":
            neighbors.append((dx, y))
            break
    # Down
    for dy in range(y + 1, HEIGHT):
        if grid[dy][x] != ".":
            neighbors.append((x, dy))
            break
    # Up
    for dy in range(y - 1, -1, -1):
        if grid[dy][x] != ".":
            neighbors.append((x, dy))
            break
    # Top Left
    xx = x
    yy = y
    while True:
        xx -= 1
        yy -= 1
        if not (0 <= xx < WIDTH and 0 <= yy < HEIGHT):
            break
        if grid[yy][xx] != ".":
            neighbors.append((xx, yy))
            break
    # Top Right
    xx = x
    yy = y
    while True:
        xx += 1
        yy -= 1
        if not (0 <= xx < WIDTH and 0 <= yy < HEIGHT):
            break
        if grid[yy][xx] != ".":
            neighbors.append((xx, yy))
            break
    # Bottom Right
    xx = x
    yy = y
    while True:
        xx += 1
        yy += 1
        if not (0 <= xx < WIDTH and 0 <= yy < HEIGHT):
            break
        if grid[yy][xx] != ".":
            neighbors.append((xx, yy))
            break
    # Bottom Left
    xx = x
    yy = y
    while True:
        xx -= 1
        yy += 1
        if not (0 <= xx < WIDTH and 0 <= yy < HEIGHT):
            break
        if grid[yy][xx] != ".":
            neighbors.append((xx, yy))
            break

    return neighbors


def count_occupied_neighbors(
    grid: list[list[str]], neighbors: list[tuple[int, int]]
) -> int:
    count = 0

    for neighbor in neighbors:
        if grid[neighbor[1]][neighbor[0]] == "#":
            count += 1

    return count


neighbors_per_tile: dict[tuple[int, int], list[tuple[int, int]]] = {}

for y in range(HEIGHT):
    for x in range(WIDTH):
        neighbors_per_tile[(x, y)] = nearby_neighbors(x, y, grid)

while True:
    next_grid = [r.copy() for r in grid]

    for y in range(HEIGHT):
        for x in range(WIDTH):
            neighbors = neighbors_per_tile[(x, y)]
            if grid[y][x] == "L" and count_occupied_neighbors(grid, neighbors) == 0:
                next_grid[y][x] = "#"
            elif grid[y][x] == "#" and count_occupied_neighbors(grid, neighbors) >= 5:
                next_grid[y][x] = "L"

    is_same = True
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if grid[y][x] != next_grid[y][x]:
                is_same = False
                break
        if not is_same:
            break

    if is_same:
        r = sum(r.count("#") for r in next_grid)
        print(f"Result: {r}")
        break

    grid = next_grid
