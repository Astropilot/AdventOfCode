from pathlib import Path

with Path(Path(__file__).parent, "sample").open() as f:
    grid = [list(line.rstrip("\n")) for line in f]


guard_positions: set[tuple[int, int]] = set()
height = len(grid)
width = len(grid[0])

guard_pos = (-1, -1)
guard_dir = None
for y in range(height):
    for x in range(width):
        if grid[y][x] in ["^", ">", "v", "<"]:
            guard_pos = (x, y)
            guard_dir = grid[y][x]
            break
    if guard_dir is not None:
        break

guard_positions.add(guard_pos)

while (0 <= guard_pos[0] < width) and (0 <= guard_pos[1] < height):
    x, y = guard_pos
    if guard_dir == "^":
        if y - 1 >= 0 and grid[y - 1][x] == "#":
            guard_dir = ">"
        else:
            guard_pos = (x, y - 1)
    if guard_dir == ">":
        if x + 1 < width and grid[y][x + 1] == "#":
            guard_dir = "v"
        else:
            guard_pos = (x + 1, y)
    if guard_dir == "v":
        if y + 1 < height and grid[y + 1][x] == "#":
            guard_dir = "<"
        else:
            guard_pos = (x, y + 1)
    if guard_dir == "<":
        if x - 1 >= 0 and grid[y][x - 1] == "#":
            guard_dir = "^"
        else:
            guard_pos = (x - 1, y)

    guard_positions.add(guard_pos)

print(f"Result: {len(guard_positions)-1}")
