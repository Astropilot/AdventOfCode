from pathlib import Path

with Path(Path(__file__).parent, "input").open() as f:
    lines = [line.rstrip("\n") for line in f]

total_pairs_overlap = 0
for line in lines:
    first_pair, second_pair = line.split(",")
    first_range, second_range = (
        list(map(int, first_pair.split("-"))),
        list(map(int, second_pair.split("-"))),
    )

    if first_range[0] >= second_range[0] and first_range[1] <= second_range[1]:
        total_pairs_overlap += 1
    elif second_range[0] >= first_range[0] and second_range[1] <= first_range[1]:
        total_pairs_overlap += 1

print(f"Result: {total_pairs_overlap}")
