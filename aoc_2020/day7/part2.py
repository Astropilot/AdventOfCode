from pathlib import Path

with Path(Path(__file__).parent, "input").open() as f:
    lines = [line.rstrip("\n") for line in f]

BAG_CONTENTS: dict[str, dict[str, int]] = {}


def compute_inner_bags(current: str) -> int:
    total = 0
    for contents in BAG_CONTENTS[current]:
        total += BAG_CONTENTS[current][contents]
        total += BAG_CONTENTS[current][contents] * compute_inner_bags(contents)

    return total


for line in lines:
    bag, other = line.split(" bags contain ")
    BAG_CONTENTS[bag] = {}

    if other == "no other bags.":
        continue

    contents = other.split(", ")
    for inner_bags in contents:
        inner = inner_bags.split(" bag")[0].split(" ", 1)[1]
        amount = int(inner_bags.split(" bag")[0].split(" ", 1)[0])

        BAG_CONTENTS[bag][inner] = amount

all_bags = compute_inner_bags("shiny gold")
print(f"Result: {all_bags}")
