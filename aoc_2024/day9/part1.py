from pathlib import Path

disk_map = Path(Path(__file__).parent, "input").read_text()

expanded: list[int] = []

# Expand
file_id = 0
for i in range(len(disk_map)):
    n = int(disk_map[i])
    if i % 2 == 0:
        expanded.extend([file_id] * n)
        file_id += 1
    else:
        expanded.extend([-1] * n)

# Moving
i_block = len(expanded) - 1
i_free = expanded.index(-1)

while i_free < i_block:
    if expanded[i_block] == -1:
        i_block -= 1
        continue

    block = expanded[i_block]
    expanded[i_block] = -1
    expanded[i_free] = block

    i_free = expanded.index(-1, i_free)
    i_block -= 1

# Checksum
checksum = 0

for i in range(len(expanded)):
    if expanded[i] == -1:
        break
    checksum += i * expanded[i]

print(f"Result: {checksum}")
