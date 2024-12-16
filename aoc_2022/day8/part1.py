from pathlib import Path

with Path(Path(__file__).parent, "input").open() as f:
    grid = [list(map(int, line.rstrip("\n"))) for line in f]

height = len(grid)
width = len(grid[0])


def is_tree_visible(x: int, y: int) -> bool:
    size = grid[y][x]
    result = True
    # Top
    for yy in range(y - 1, -1, -1):
        if grid[yy][x] >= size:
            result = False
            break
    if result:
        return True
    result = True
    # Bottom
    for yy in range(y + 1, height, 1):
        if grid[yy][x] >= size:
            result = False
            break
    if result:
        return True
    result = True
    # Left
    for xx in range(x - 1, -1, -1):
        if grid[y][xx] >= size:
            result = False
            break
    if result:
        return True
    # Right
    for xx in range(x + 1, width, 1):
        if grid[y][xx] >= size:
            return False

    return True


total_trees_visible = 0
for y in range(height):
    for x in range(width):
        if is_tree_visible(x, y):
            total_trees_visible += 1

print(f"Result: {total_trees_visible}")  # Result: 1792
