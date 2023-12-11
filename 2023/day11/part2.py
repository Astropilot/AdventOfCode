from itertools import combinations
from pathlib import Path

contents = Path(Path(__file__).parent, "input").read_text()
lines = contents.split("\n")

EXPANSION = 1000000 - 1
galaxies: list[tuple[int, int]] = []
blank_lines: list[int] = []
blank_columns: list[int] = []

for y in range(len(lines)):
    is_blank_line = True
    for x in range(len(lines[y])):
        if lines[y][x] == "#":
            is_blank_line = False
            galaxies.append((x, y))
    if is_blank_line:
        blank_lines.append(y)

for x in range(len(lines[0])):
    is_blank_col = True
    for y in range(len(lines)):
        if lines[y][x] == "#":
            is_blank_col = False
            break
    if is_blank_col:
        blank_columns.append(x)

sum_paths = 0
for galaxy1, galaxy2 in combinations(galaxies, 2):
    expanded_galaxy1 = (
        galaxy1[0]
        + (len(list(filter(lambda c: c < galaxy1[0], blank_columns))) * EXPANSION),
        galaxy1[1]
        + (len(list(filter(lambda c: c < galaxy1[1], blank_lines))) * EXPANSION),
    )
    expanded_galaxy2 = (
        galaxy2[0]
        + (len(list(filter(lambda c: c < galaxy2[0], blank_columns))) * EXPANSION),
        galaxy2[1]
        + (len(list(filter(lambda c: c < galaxy2[1], blank_lines))) * EXPANSION),
    )
    d = abs(expanded_galaxy2[0] - expanded_galaxy1[0]) + abs(
        expanded_galaxy2[1] - expanded_galaxy1[1]
    )

    sum_paths += d

print(f"Result: {sum_paths}")  # Result: 726820169514
