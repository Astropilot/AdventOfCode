import re
from pathlib import Path

contents = Path(Path(__file__).parent, "input").read_text()

total = 0

enabled = True
for m in re.findall(r"(don't\(\))|(mul\((\d+),(\d+)\))|(do\(\))", contents):
    if m[0] == "don't()":
        enabled = False
    elif m[4] == "do()":
        enabled = True
    elif enabled:
        total += int(m[2]) * int(m[3])

print(f"Result: {total}")
