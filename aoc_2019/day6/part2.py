from pathlib import Path

adj_list: dict[str, list[str]] = {}

with Path(Path(__file__).parent, "input").open() as f:
    orbits_raw = [line.rstrip("\n") for line in f]

for raw in orbits_raw:
    a, b = raw.split(")")
    adj_list.setdefault(a, []).append(b)
    adj_list.setdefault(b, []).append(a)

q: list[str] = []
visited: set[str] = set()
start = adj_list["YOU"][0]
stop = adj_list["SAN"][0]

visited.add(start)
q.append(start)
distance: dict[str, int] = {start: 0}

while len(q):
    v = q.pop(0)

    if v == stop:
        break

    for w in adj_list[v]:
        if w not in visited:
            visited.add(w)
            distance[w] = distance[v] + 1
            q.append(w)

print(f"Result: {distance[stop]}")
