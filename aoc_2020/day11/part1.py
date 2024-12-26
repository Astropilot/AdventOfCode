from pathlib import Path

with Path(Path(__file__).parent, "input").open() as f:
    grid = [list(line.rstrip("\n")) for line in f]

HEIGHT = len(grid)
WIDTH = len(grid[0])


def count_occupied_neighbors(x: int, y: int, grid: list[list[str]]) -> int:
    count = 0

    for dx, dy in (
        (0, -1),
        (1, -1),
        (1, 0),
        (1, 1),
        (0, 1),
        (-1, 1),
        (-1, 0),
        (-1, -1),
    ):
        if 0 <= x + dx < WIDTH and 0 <= y + dy < HEIGHT:
            if grid[y + dy][x + dx] == "#":
                count += 1

    return count


while True:
    next_grid = [r.copy() for r in grid]

    for y in range(HEIGHT):
        for x in range(WIDTH):
            if grid[y][x] == "L" and count_occupied_neighbors(x, y, grid) == 0:
                next_grid[y][x] = "#"
            elif grid[y][x] == "#" and count_occupied_neighbors(x, y, grid) >= 4:
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
