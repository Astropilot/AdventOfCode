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


total_secrets = 0

for seed in seeds:
    secret = seed
    for _ in range(2000):
        secret = generate_next(secret)

    total_secrets += secret

print(f"Result: {total_secrets}")  # Result: 18261820068
