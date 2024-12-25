from pathlib import Path

with Path(Path(__file__).parent, "input").open() as f:
    lines = [line.rstrip("\n") for line in f]

i = 0
locks: set[tuple[int, int, int, int, int]] = set()
keys: set[tuple[int, int, int, int, int]] = set()

while i < len(lines):
    pattern = lines[i : i + 7]
    if lines[i] == "#####":
        pattern = list(reversed(pattern))
    pattern = pattern[1:]

    pattern_cols = [-1, -1, -1, -1, -1]
    for i_pattern in range(len(pattern)):
        if pattern_cols[0] == -1 and pattern[i_pattern][0] == "#":
            pattern_cols[0] = 5 - i_pattern
        if pattern_cols[1] == -1 and pattern[i_pattern][1] == "#":
            pattern_cols[1] = 5 - i_pattern
        if pattern_cols[2] == -1 and pattern[i_pattern][2] == "#":
            pattern_cols[2] = 5 - i_pattern
        if pattern_cols[3] == -1 and pattern[i_pattern][3] == "#":
            pattern_cols[3] = 5 - i_pattern
        if pattern_cols[4] == -1 and pattern[i_pattern][4] == "#":
            pattern_cols[4] = 5 - i_pattern
    if lines[i] == "#####":
        locks.add(tuple(pattern_cols))  # type: ignore
    else:
        keys.add(tuple(pattern_cols))  # type: ignore

    i += 8

fit_count = 0
for key in keys:
    for lock in locks:
        res = (
            key[0] + lock[0],
            key[1] + lock[1],
            key[2] + lock[2],
            key[3] + lock[3],
            key[4] + lock[4],
        )
        if all(r <= 5 for r in res):
            fit_count += 1

print(f"Result: {fit_count}")
