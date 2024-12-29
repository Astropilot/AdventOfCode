from pathlib import Path

with Path(Path(__file__).parent, "input").open() as f:
    jumps = [int(line.rstrip("\n")) for line in f]

i = 0
steps = 0

while 0 <= i < len(jumps):
    old_i = i
    i += jumps[i]
    if jumps[old_i] >= 3:
        jumps[old_i] -= 1
    else:
        jumps[old_i] += 1
    steps += 1

print(f"Result: {steps}")
