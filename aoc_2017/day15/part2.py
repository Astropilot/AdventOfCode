import typing as t
from itertools import islice
from pathlib import Path

with Path(Path(__file__).parent, "input").open() as f:
    lines = [line.rstrip("\n") for line in f]

seed_a = int(lines[0].split(" with ")[1])
seed_b = int(lines[1].split(" with ")[1])
judge_count = 0


def generator_a() -> t.Generator[int, t.Any, t.NoReturn]:
    global seed_a

    while True:
        seed_a = (seed_a * 16807) % 2147483647

        if seed_a % 4 == 0:
            yield seed_a


def generator_b() -> t.Generator[int, t.Any, t.NoReturn]:
    global seed_b

    while True:
        seed_b = (seed_b * 48271) % 2147483647

        if seed_b % 8 == 0:
            yield seed_b


for value_a, value_b in islice(zip(generator_a(), generator_b(), strict=True), 5000000):
    if value_a & 0xFFFF == value_b & 0xFFFF:
        judge_count += 1


print(f"Result: {judge_count}")
