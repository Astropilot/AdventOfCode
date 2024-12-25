from itertools import product
from pathlib import Path

with Path(Path(__file__).parent, "input").open() as f:
    numbers = [int(line.rstrip("\n")) for line in f]


def find_pair_equals(n: int, choices: list[int]) -> bool:
    for n1, n2 in product(choices, choices):
        if n1 != n2 and n1 + n2 == n:
            return True
    return False


invalid_number = -1
for i in range(25, len(numbers)):
    n = numbers[i]

    if not find_pair_equals(n, numbers[i - 25 : i]):
        invalid_number = n
        break

s_invalid: set[int] = set()
for i in range(0, len(numbers)):
    contiguous_set: set[int] = {numbers[i]}
    sum_set = numbers[i]
    found = False
    for j in range(i + 1, len(numbers)):
        sum_set += numbers[j]
        contiguous_set.add(numbers[j])

        if sum_set == invalid_number:
            found = True
            s_invalid = contiguous_set
            break
        if sum_set > invalid_number:
            break
    if found:
        break

print(f"Result: {min(s_invalid) + max(s_invalid)}")
