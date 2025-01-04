from pathlib import Path

with Path(Path(__file__).parent, "input").open() as f:
    lines = [line.rstrip("\n") for line in f]

seed_a = int(lines[0].split(" with ")[1])
seed_b = int(lines[1].split(" with ")[1])
judge_count = 0

for _ in range(40000000):
    seed_a = (seed_a * 16807) % 2147483647
    seed_b = (seed_b * 48271) % 2147483647

    if seed_a & 0xFFFF == seed_b & 0xFFFF:
        judge_count += 1


print(f"Result: {judge_count}")
