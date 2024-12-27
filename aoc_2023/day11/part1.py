from itertools import combinations
from pathlib import Path
from typing import Literal, cast

contents = Path(Path(__file__).parent, "input").read_text()
lines = contents.split("\n")

map_universe: list[list[Literal[".", "#"]]] = []

for y in range(len(lines)):
    map_universe.append([])
    is_blank_line = True
    for x in range(len(lines[y])):
        if lines[y][x] == "#":
            is_blank_line = False
        map_universe[-1].append(cast(Literal[".", "#"], lines[y][x]))
    if is_blank_line:
        map_universe.append(["." for _ in range(len(lines[y]))])

decal = 0
for x in range(len(map_universe[0])):
    is_blank_col = True
    for y in range(len(map_universe)):
        if map_universe[y][x + decal] == "#":
            is_blank_col = False
            break

    if is_blank_col:
        for y in range(len(map_universe)):
            map_universe[y].insert(x + decal + 1, ".")
        decal += 1

galaxies: list[tuple[int, int]] = []

for y in range(len(map_universe)):
    for x in range(len(map_universe[y])):
        if map_universe[y][x] == "#":
            galaxies.append((x, y))

sum_paths = 0
for galaxy1, galaxy2 in combinations(galaxies, 2):
    d = abs(galaxy2[0] - galaxy1[0]) + abs(galaxy2[1] - galaxy1[1])

    sum_paths += d

print(f"Result: {sum_paths}")
