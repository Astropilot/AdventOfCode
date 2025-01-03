from collections import Counter
from pathlib import Path

with Path(Path(__file__).parent, "input").open() as f:
    lines = [list(line.rstrip("\n")) for line in f]

message = ""

for column in zip(*lines, strict=True):
    counter = Counter(column)

    message += sorted(counter.keys(), key=lambda k: counter[k], reverse=True)[0]

print(f"Result: {message}")
