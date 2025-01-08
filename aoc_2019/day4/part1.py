from itertools import pairwise
from pathlib import Path

start, stop = [
    int(c) for c in Path(Path(__file__).parent, "input").read_text().split("-")
]

count = 0
for candidate in range(start, stop + 1):
    candidate_str = str(candidate)
    has_adj_digits = False
    never_decrease = True

    for c1, c2 in pairwise(candidate_str):
        if c1 == c2:
            has_adj_digits = True
        if int(c1) > int(c2):
            never_decrease = False
    if has_adj_digits and never_decrease:
        count += 1

print(f"Result: {count}")
