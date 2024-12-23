from pathlib import Path

with Path(Path(__file__).parent, "input").open() as f:
    lines = [line.rstrip("\n") for line in f]

adj_list: dict[str, list[str]] = {}
pc_sets: dict[str, list[frozenset[str]]] = {}

for line in lines:
    pc1, pc2 = line.split("-")

    adj_list.setdefault(pc1, []).append(pc2)
    adj_list.setdefault(pc2, []).append(pc1)

sets: set[frozenset[str]] = set()
for pc in adj_list:
    for neighbor1 in adj_list[pc]:
        for neighbor2 in adj_list[neighbor1]:
            if pc in adj_list[neighbor2]:
                sets.add(frozenset((pc, neighbor1, neighbor2)))

results = [s for s in sets if any(pc[0] == "t" for pc in s)]

print(f"Result: {len(results)}")  # Result: 1337
