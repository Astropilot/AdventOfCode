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

visited: set[str] = set()
queue: list[str] = []

visited.add("0")
queue.append("0")

while len(queue) > 0:
    v = queue.pop()

    for neighbor in adj_list[v]:
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)

print(f"Result: {len(visited)}")
