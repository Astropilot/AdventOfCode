from pathlib import Path

with Path(Path(__file__).parent, "input").open() as f:
    lines = [line.rstrip("\n") for line in f]

program = list(map(int, lines[4].removeprefix("Program: ").split(",")))

# Pattern (extracted from output file generated by part1.py with DEBUG=True)
# B = A % 8
# B = B ^ 3
# C = A // (2 ** B)
# A = A // (2 ** 3)
# B = B ^ C
# B = B ^ 5
# out B % 8


def check_ra_match(ra: int, wanted: int) -> bool:
    rb = ra % 8
    rb = rb ^ 3
    rc = ra // (2**rb)
    rb = rb ^ rc
    rb = rb ^ 5

    return rb % 8 == wanted


def resolve_ra(program: list[int]) -> int | None:
    candidates: set[int] = {0}

    for output in reversed(program):
        candidates_output: set[int] = set()

        for candidate in candidates:
            ra = candidate * (2**3)

            for i in range(8):
                rai = ra + i
                if check_ra_match(rai, output):
                    candidates_output.add(rai)
        if len(candidates_output) == 0:
            return None
        else:
            candidates = candidates_output

    return min(candidates)


print(f"Result: {resolve_ra(program)}")
