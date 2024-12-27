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

            antinodes.add(first_antenna)
            antinodes.add(second_antenna)

            last_antinode_pos = first_antenna
            delta_x = first_antenna.x - second_antenna.x
            delta_y = first_antenna.y - second_antenna.y

            while True:
                antinode1 = Coords(
                    last_antinode_pos.x + delta_x,
                    last_antinode_pos.y + delta_y,
                )
                if (0 <= antinode1.x < width) and (0 <= antinode1.y < height):
                    antinodes.add(antinode1)
                    last_antinode_pos = antinode1
                else:
                    break

            last_antinode_pos = second_antenna
            delta_x = second_antenna.x - first_antenna.x
            delta_y = second_antenna.y - first_antenna.y

            while True:
                antinode2 = Coords(
                    last_antinode_pos.x + delta_x,
                    last_antinode_pos.y + delta_y,
                )
                if (0 <= antinode2.x < width) and (0 <= antinode2.y < height):
                    antinodes.add(antinode2)
                    last_antinode_pos = antinode2
                else:
                    break

print(f"Result: {len(antinodes)}")
