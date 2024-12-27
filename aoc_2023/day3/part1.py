import re
from pathlib import Path

contents = Path(Path(__file__).parent, "input").read_text()

#                       position     len  number
numbers: list[tuple[tuple[int, int], int, int]] = []
symbols: list[tuple[int, int]] = []

sum_numbers = 0

for idx, line in enumerate(contents.split("\n")):
    for m in re.finditer(r"\d+", line):
        numbers.append(((m.start(), idx), m.end() - m.start(), int(m.group(0))))
    for m in re.finditer(r"[^\d.]+", line):
        symbols.append((m.start(), idx))

for n in numbers:
    p = filter(
        lambda s: (s[0] == n[0][0] - 1 and s[1] == n[0][1])  # left
        or any(s[0] == n[0][0] + i and s[1] == n[0][1] - 1 for i in range(n[1]))  # top
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

    if len(list(p)) > 0:
        sum_numbers += n[2]


print(f"Result: {sum_numbers}")
