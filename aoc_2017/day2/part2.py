from itertools import product
from pathlib import Path

with Path(Path(__file__).parent, "input").open() as f:
    rows = [line.rstrip("\n") for line in f]

sum_divisions = 0

for row in rows:
    numbers = [int(n) for n in row.split("\t")]

    for n1, n2 in product(numbers, numbers):
        if n1 == n2:
            continue
        if n1 % n2 == 0:
            sum_divisions += n1 // n2
            break

print(f"Result: {sum_divisions}")
