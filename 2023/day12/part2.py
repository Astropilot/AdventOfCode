# from functools import cache
from pathlib import Path

contents = Path(Path(__file__).parent, "sample").read_text()
lines = contents.split("\n")


# @cache
def rec_arrangements(
    springs_with_start: tuple[str, int], contiguous: tuple[int, ...]
) -> list[tuple[str, int]]:
    if len(contiguous) == 1:
        n = contiguous[0]
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

            possibilities.append((possibility, i + n))
            # for j in range(n):
            #     if possibility[i + j] == "?":
            #         possibility = possibility[: i + j] + "#" + possibility[i + j + 1 :]

        return possibilities
    else:
        possibilities: list[tuple[str, int]] = [springs_with_start]
        for cont in contiguous:
            new_possibilities: list[tuple[str, int]] = []

            for possibility in possibilities:
                new_possibilities.extend(rec_arrangements(possibility, (cont,)))

            # print(f"For {cont}:")
            # for p in new_possibilities:
            #     print(f"\t{p}")
            possibilities = new_possibilities

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

    # springs = tuple([s for s in springs_conditions.split(".") if len(s) > 0])

    arrangements = rec_arrangements((springs_conditions, 0), tuple(contiguous_groups))

    print(f"{springs_conditions} {contiguous_groups} - {len(arrangements)}")

    sum_arrangements += len(arrangements)


print(f"Result: {sum_arrangements}")  # Result: 6827
