# from functools import cache
from pathlib import Path

contents = Path(Path(__file__).parent, "sample").read_text()
lines = contents.split("\n")


# @cache
def rec_arrangements(
    springs_with_start: tuple[str, int],
    contiguous: tuple[int, ...],
    current_contiguous: int,
) -> list[tuple[str, int]]:
    if current_contiguous >= len(contiguous):
        return [springs_with_start]

    n = contiguous[current_contiguous]
    possibilities: list[tuple[str, int]] = []
    springs = springs_with_start[0]
    start = springs_with_start[1]

    for i in range(start, len(springs) - (n - 1)):
        possibility = springs

        if i - 1 >= start:
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

        possibility = (
            possibility[:i].replace("?", ".") + ("#" * n) + possibility[i + n :]
        )

        assert len(possibility) == len(springs)

        print(
            f"For {n} ({current_contiguous}) trying possibility {(possibility, i + n)}"
        )

        new_possibilities = rec_arrangements(
            (possibility, i + n), contiguous, current_contiguous + 1
        )

        for p in new_possibilities:
            print(f"\tFor {n} ({current_contiguous}): {p}")

        possibilities.extend(new_possibilities)

    # print(f"For {n} ({current_contiguous}):")
    # for p in possibilities:
    #     print(f"\t{p}")

    return possibilities


rec_arrangements(("?###????????", 0), (3, 2, 1), 0)


# sum_arrangements = 0
# for line in lines:
#     springs_conditions, contiguous_groups = (
#         line.split(" ")[0],
#         list(map(int, line.split(" ")[1].split(","))),
#     )

#     # springs_conditions = "?".join([springs_conditions for _ in range(5)])
#     # new_contiguous_groups: list[int] = []
#     # for _ in range(5):
#     #     new_contiguous_groups.extend(contiguous_groups)
#     # contiguous_groups = new_contiguous_groups

#     # springs = tuple([s for s in springs_conditions.split(".") if len(s) > 0])

#     arrangements = rec_arrangements(
#         (springs_conditions, 0), tuple(contiguous_groups), 0
#     )

#     print(f"{springs_conditions} {contiguous_groups} - {len(arrangements)}")

#     sum_arrangements += len(arrangements)


# print(f"Result: {sum_arrangements}")  # Result: 6827
