from pathlib import Path

with Path(Path(__file__).parent, "input").open() as f:
    grid = [list(map(int, line.rstrip("\n"))) for line in f]

HEIGHT = len(grid)
WIDTH = len(grid[0])

total_risk_levels = 0
for y in range(HEIGHT):
    for x in range(WIDTH):
        is_low = True
        for dx, dy in ((0, -1), (1, 0), (0, 1), (-1, 0)):
            xx = x + dx
            yy = y + dy
            if 0 <= xx < WIDTH and 0 <= yy < HEIGHT and grid[yy][xx] <= grid[y][x]:
                is_low = False
                break
        if is_low:
            total_risk_levels += 1 + grid[y][x]

print(f"Result: {total_risk_levels}")
