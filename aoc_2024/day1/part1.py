from pathlib import Path

with Path(Path(__file__).parent, "input").open() as f:
    lines_splitted = [line.split("   ") for line in f]


left_list = sorted([int(i[0]) for i in lines_splitted])
right_list = sorted([int(i[1]) for i in lines_splitted])

distance = sum(
    abs(left - right) for left, right in zip(left_list, right_list, strict=True)
)

print(f"Result: {distance}")
