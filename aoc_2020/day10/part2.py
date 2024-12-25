from pathlib import Path

with Path(Path(__file__).parent, "input").open() as f:
    adapters = {int(line.rstrip("\n")) for line in f}

device_adapter = max(adapters) + 3


def compute_arrangements(
    rating: int, adapters: frozenset[int], memoize: dict[int, int]
) -> int:
    if rating in memoize:
        return memoize[rating]
    if rating == device_adapter:
        memoize[rating] = 1
        return 1

    candidates = [
        a for a in adapters if a in (rating, rating + 1, rating + 2, rating + 3)
    ]

    arrangements = 0
    for candidate in candidates:
        adapters_without_candidate = adapters.difference({candidate})

        arrangements += compute_arrangements(
            candidate, adapters_without_candidate, memoize
        )

    memoize[rating] = arrangements
    return arrangements


adapters.add(device_adapter)

arrangements = compute_arrangements(0, frozenset(adapters), {})

print(f"Result: {arrangements}")
