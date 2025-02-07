from collections import Counter
from pathlib import Path

with Path(Path(__file__).parent, "input").open() as f:
    lines = [line.rstrip("\n") for line in f]

counter_two = 0
counter_three = 0

for id in lines:
    c = Counter(id)

    if any(v == 2 for v in c.values()):
        counter_two += 1
    if any(v == 3 for v in c.values()):
        counter_three += 1

print(f"Result: {counter_two * counter_three}")
