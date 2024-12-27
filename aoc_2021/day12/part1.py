from pathlib import Path

with Path(Path(__file__).parent, "input").open() as f:
    lines = [line.rstrip("\n") for line in f]

MAPPING: dict[str, list[str]] = {}

for line in lines:
    start, end = line.split("-")

    dest_start = MAPPING.setdefault(start, [])
    dest_start.append(end)

    dest_end = MAPPING.setdefault(end, [])
    dest_end.append(start)


def count_path_from(cave: str, visited: set[str]) -> int:
    if cave == "end":
        return 1

    visited = visited.union([cave])
    paths = 0

    for neighbor in MAPPING[cave]:
        if neighbor.isupper() or neighbor not in visited:
            paths += count_path_from(neighbor, visited)

    return paths


paths = count_path_from("start", set())

print(f"Result: {paths}")
