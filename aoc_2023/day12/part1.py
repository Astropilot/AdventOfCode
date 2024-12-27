from itertools import product
from pathlib import Path

contents = Path(Path(__file__).parent, "input").read_text()
lines = contents.split("\n")

sum_arrangements = 0
for line in lines:
    springs_conditions, contiguous_groups = (
        line.split(" ")[0],
        list(map(int, line.split(" ")[1].split(","))),
    )

    if "?" not in springs_conditions:
        sum_arrangements += 1
        continue

    perms = product(".#", repeat=springs_conditions.count("?"))
    hashtag_count = springs_conditions.count("#")
    sum_hashtag = sum(contiguous_groups)

    for perm in perms:
        if perm.count("#") + hashtag_count != sum_hashtag:
            continue
        springs_condition_perm = springs_conditions
        for i in range(len(perm)):
            springs_condition_perm = springs_condition_perm.replace("?", perm[i], 1)

        groups = [p for p in springs_condition_perm.split(".") if len(p) > 0]

        if len(groups) != len(contiguous_groups):
            continue

        is_ok = True
        for i in range(len(groups)):
            if groups[i].count("#") != contiguous_groups[i]:
                is_ok = False
                break
        if is_ok:
            sum_arrangements += 1

print(f"Result: {sum_arrangements}")
