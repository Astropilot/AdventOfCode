import re
from pathlib import Path

contents = Path(Path(__file__).parent, "input").read_text()

#                       position     len  number
possible_parts: list[tuple[tuple[int, int], int, int]] = []
#                    x    y   possible_gear
symbols: list[tuple[int, int, bool]] = []

adjacency: dict[tuple[int, int], list[tuple[tuple[int, int], int, int]]] = {}

sum_gear_ratio = 0

for idx, line in enumerate(contents.split("\n")):
    for m in re.finditer(r"\d+", line):
        possible_parts.append(((m.start(), idx), m.end() - m.start(), int(m.group(0))))
    for m in re.finditer(r"[^\d.]+", line):
        symbols.append((m.start(), idx, m.group(0) == "*"))

for n in possible_parts:
    p = list(
        filter(
            lambda s: (s[0] == n[0][0] - 1 and s[1] == n[0][1])  # left
            or any(
                s[0] == n[0][0] + i and s[1] == n[0][1] - 1 for i in range(n[1])
            )  # top
            or (s[0] == n[0][0] + n[1] and s[1] == n[0][1])  # right
            or any(
                s[0] == n[0][0] + i and s[1] == n[0][1] + 1 for i in range(n[1])
            )  # bottom
            or (s[0] == n[0][0] - 1 and s[1] == n[0][1] - 1)  # top-left
            or (s[0] == n[0][0] + n[1] and s[1] == n[0][1] - 1)  # top-right
            or (s[0] == n[0][0] - 1 and s[1] == n[0][1] + 1)  # bottom-left
            or (s[0] == n[0][0] + n[1] and s[1] == n[0][1] + 1),  # bottom-right
            symbols,
        )
    )

    for symbol in p:
        t = (symbol[0], symbol[1])

        if t in adjacency:
            adjacency[t].append(n)
        else:
            adjacency[t] = [n]

for pg in filter(lambda s: s[2], symbols):
    t = (pg[0], pg[1])

    if t in adjacency:
        parts = adjacency[t]

        if len(parts) == 2:
            sum_gear_ratio += parts[0][2] * parts[1][2]


print(f"Result: {sum_gear_ratio}")
