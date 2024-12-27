from pathlib import Path

with Path(Path(__file__).parent, "input").open() as f:
    seeds = [int(line.rstrip("\n")) for line in f]


def generate_next(secret: int) -> int:
    step1 = secret * 64
    secret = (step1 ^ secret) % 16777216
    step2 = secret // 32
    secret = (step2 ^ secret) % 16777216
    step3 = secret * 2048
    secret = (step3 ^ secret) % 16777216

    return secret


sequences_to_prices: dict[tuple[int, int, int, int], int] = {}
for seed in seeds:
    prices_changes: list[int] = [int(str(seed)[-1])]
    secret = seed
    for _ in range(2000):
        secret = generate_next(secret)
        prices_changes.append(int(str(secret)[-1]))

    visited_sequences: set[tuple[int, int, int, int]] = set()
    for price_i in range(4, len(prices_changes)):
        sequence = (
            prices_changes[price_i - 3] - prices_changes[price_i - 4],
            prices_changes[price_i - 2] - prices_changes[price_i - 3],
            prices_changes[price_i - 1] - prices_changes[price_i - 2],
            prices_changes[price_i] - prices_changes[price_i - 1],
        )
        if sequence not in visited_sequences:
            sequences_to_prices[sequence] = (
                sequences_to_prices.setdefault(sequence, 0) + prices_changes[price_i]
            )
            visited_sequences.add(sequence)

best_sequence = max(sequences_to_prices, key=lambda k: sequences_to_prices[k])

print(f"Result: {sequences_to_prices[best_sequence]}")
