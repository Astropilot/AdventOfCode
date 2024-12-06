from functools import cache
from pathlib import Path

contents = Path(Path(__file__).parent, "input").read_text()
lines = contents.split("\n")


@cache
def rec_arrangements(springs: str, contiguous: tuple[int, ...]) -> int:
    n = contiguous[0]
    possibilities: int = 0

    needed_space = n
    for m in contiguous[1:]:
        needed_space += 1 + m

    try:
        max_idx = springs.index("#") + 1
    except ValueError:
        max_idx = len(springs) - (n - 1)

    for i in range(max_idx):
        if i + needed_space > len(springs):
            break

        possibility = springs

        if i - 1 >= 0:
            if possibility[i - 1] == "#":
                continue
            if possibility[i - 1] == "?":
                possibility = possibility[: i - 1] + "." + possibility[i:]
        if (i + n) <= len(possibility) - 1:
            if possibility[i + n] == "#":
                continue
            if possibility[i + n] == "?":
                possibility = possibility[: i + n] + "." + possibility[i + n + 1 :]

        if "." in possibility[i : i + n]:
            continue

        if len(contiguous) > 1:
            possibilities += rec_arrangements(springs[i + n + 1 :], contiguous[1:])
        else:
            if "#" not in springs[i + n + 1 :]:
                possibilities += 1

    return possibilities


sum_arrangements = 0
for line in lines:
    springs_conditions, contiguous_groups = (
        line.split(" ")[0],
        list(map(int, line.split(" ")[1].split(","))),
    )

    springs_conditions = "?".join([springs_conditions for _ in range(5)])
    new_contiguous_groups: list[int] = []
    for _ in range(5):
        new_contiguous_groups.extend(contiguous_groups)
    contiguous_groups = new_contiguous_groups

    arrangements = rec_arrangements(springs_conditions, tuple(contiguous_groups))

    sum_arrangements += arrangements


print(f"Result: {sum_arrangements}")  # Result: 1537505634471
