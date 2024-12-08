from pathlib import Path
from typing import NamedTuple

with Path(Path(__file__).parent, "input").open() as f:
    lines = [line.rstrip("\n") for line in f]


class Coords(NamedTuple):
    x: int
    y: int


height = len(lines)
width = len(lines[0])
antennas_by_frequency: dict[str, list[Coords]] = {}

for y, line in enumerate(lines):
    for x in range(len(line)):
        if line[x] != ".":
            if line[x] not in antennas_by_frequency:
                antennas_by_frequency[line[x]] = []
            antennas_by_frequency[line[x]].append(Coords(x, y))

antinodes: set[Coords] = set()
for antennas in antennas_by_frequency.values():
    for i in range(len(antennas)):
        for j in range(i + 1, len(antennas)):
            first_antenna = antennas[i]
            second_antenna = antennas[j]

            antinode1 = Coords(
                first_antenna.x + (first_antenna.x - second_antenna.x),
                first_antenna.y + (first_antenna.y - second_antenna.y),
            )
            antinode2 = Coords(
                second_antenna.x + (second_antenna.x - first_antenna.x),
                second_antenna.y + (second_antenna.y - first_antenna.y),
            )
            if (0 <= antinode1.x < width) and (0 <= antinode1.y < height):
                antinodes.add(antinode1)
            if (0 <= antinode2.x < width) and (0 <= antinode2.y < height):
                antinodes.add(antinode2)

print(f"Result: {len(antinodes)}")  # Result: 280
