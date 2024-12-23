from pathlib import Path

with Path(Path(__file__).parent, "input").open() as f:
    lines = [line.rstrip("\n") for line in f]

BAG_PARENT: dict[str, list[str]] = {}


def compute_outer_bags(current: str) -> set[str]:
    if current not in BAG_PARENT or len(BAG_PARENT[current]) == 0:
        return {current}

    res: set[str] = {current}

    for p in BAG_PARENT[current]:
        res = res.union(compute_outer_bags(p))

    return res


for line in lines:
    bag, other = line.split(" bags contain ")
    if other == "no other bags.":
        continue
    contents = other.split(", ")
    for inner_bags in contents:
        inner = inner_bags.split(" bag")[0].split(" ", 1)[1]

        BAG_PARENT.setdefault(inner, []).append(bag)

all_bags: set[str] = set()
for parent in BAG_PARENT["shiny gold"]:
    all_bags = all_bags.union(compute_outer_bags(parent))

print(f"Result: {len(all_bags)}")
