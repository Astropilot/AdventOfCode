from pathlib import Path

with Path(Path(__file__).parent, "input").open() as f:
    grid = [list(map(int, line.rstrip("\n"))) for line in f]

height = len(grid)
width = len(grid[0])


def tree_scenic_score(x: int, y: int) -> int:
    size = grid[y][x]
    scenic_score = 1

    # Top
    score = 0
    for yy in range(y - 1, -1, -1):
        score += 1
        if grid[yy][x] >= size:
            break
    scenic_score *= score

    # Bottom
    score = 0
    for yy in range(y + 1, height, 1):
        score += 1
        if grid[yy][x] >= size:
            break
    scenic_score *= score

    # Left
    score = 0
    for xx in range(x - 1, -1, -1):
        score += 1
        if grid[y][xx] >= size:
            break
    scenic_score *= score

    # Right
    score = 0
    for xx in range(x + 1, width, 1):
        score += 1
        if grid[y][xx] >= size:
            break
    scenic_score *= score

    return scenic_score


highest_scenic_score = 0
for y in range(height):
    for x in range(width):
        scenic_score = tree_scenic_score(x, y)
        if scenic_score > highest_scenic_score:
            highest_scenic_score = scenic_score

print(f"Result: {highest_scenic_score}")
