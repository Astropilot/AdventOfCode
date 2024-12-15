from pathlib import Path

with Path(Path(__file__).parent, "input").open() as f:
    lines = [line.rstrip("\n") for line in f]

delimiter_idx = lines.index("")

crates_count = len(lines[delimiter_idx - 1].split("   "))

crates: list[list[str]] = [[] for _ in range(crates_count)]

for i in range(delimiter_idx - 2, -1, -1):
    line = lines[i]
    crate = 0
    for j in range(1, len(line), 4):
        if line[j] != " ":
            crates[crate].append(line[j])
        crate += 1

for line in lines[delimiter_idx + 1 :]:
    _, count, _, from_crate, _, to_crate = line.split(" ")

    elements: list[str] = []
    for __ in range(int(count)):
        elements.insert(0, crates[int(from_crate) - 1].pop())

    crates[int(to_crate) - 1].extend(elements)

message = ""

for c in crates:
    if len(c) > 0:
        message += c[-1]

print(f"Result: {message}")  # Result: ZFSJBPRFP
