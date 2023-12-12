from itertools import product
from pathlib import Path

contents = Path(Path(__file__).parent, "sample").read_text()
lines = contents.split("\n")

sum_arrangements = 0
for line in lines:
    springs_conditions, contiguous_groups = (
        line.split(" ")[0],
        list(map(int, line.split(" ")[1].split(","))),
    )

    # springs_conditions = "?".join([springs_conditions for _ in range(5)])
    # new_contiguous_groups: list[int] = []
    # for _ in range(5):
    #     new_contiguous_groups.extend(contiguous_groups)
    # contiguous_groups = new_contiguous_groups

    if "?" not in springs_conditions:
        sum_arrangements += 1
        continue


print(f"Result: {sum_arrangements}")  # Result: 6827
