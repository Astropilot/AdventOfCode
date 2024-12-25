from itertools import product
from pathlib import Path

with Path(Path(__file__).parent, "input").open() as f:
    numbers = [int(line.rstrip("\n")) for line in f]


def find_pair_equals(n: int, choices: list[int]) -> bool:
    for n1, n2 in product(choices, choices):
        if n1 != n2 and n1 + n2 == n:
            return True
    return False


for i in range(25, len(numbers)):
    n = numbers[i]

    if not find_pair_equals(n, numbers[i - 25 : i]):
        print(f"Result: {n}")
        break
