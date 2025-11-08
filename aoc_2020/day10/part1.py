from itertools import pairwise
from pathlib import Path

with Path(Path(__file__).parent, "input").open() as f:
    adapters = {int(line.rstrip("\n")) for line in f}

device_adapter = max(adapters) + 3


def compute_sequence(rating: int, adapters: frozenset[int]) -> list[int]:
    if rating == device_adapter and len(adapters) == 0:
        return [device_adapter]

    candidates = [
        a for a in adapters if a in (rating, rating + 1, rating + 2, rating + 3)
    ]

    for candidate in candidates:
        adapters_without_candidate = adapters.difference({candidate})

        r = compute_sequence(candidate, adapters_without_candidate)

        if len(r) > 0:
            return [candidate, *r]

    return []


adapters.add(device_adapter)

seq = [0, *compute_sequence(0, frozenset(adapters))[:-1]]

diffs: list[int] = []
for a1, a2 in pairwise(seq):
    diffs.append(a2 - a1)

diffs_1_len = len([d for d in diffs if d == 1])
diffs_3_len = len([d for d in diffs if d == 3])

print(f"Result: {diffs_1_len * diffs_3_len}")
