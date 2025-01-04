from pathlib import Path

with Path(Path(__file__).parent, "input").open() as f:
    lines = [line.rstrip("\n") for line in f]

adj_list: dict[str, set[str]] = {}

for line in lines:
    program, neighbors_list = line.split(" <-> ")
    if "," in neighbors_list:
        neighbors = neighbors_list.split(", ")
    else:
        neighbors = [neighbors_list]

    s = adj_list.setdefault(program, set())
    for neighbor in neighbors:
        s.add(neighbor)


def bfs(visited: set[str], start: str, adj_list: dict[str, set[str]]) -> None:
    queue: list[str] = []

    visited.add(start)
    queue.append(start)

    while len(queue) > 0:
        v = queue.pop()

        for neighbor in adj_list[v]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


visited: set[str] = set()
groups = 0

for program in adj_list:
    if program in visited:
        continue

    bfs(visited, program, adj_list)
    groups += 1

print(f"Result: {groups}")
