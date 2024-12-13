import re
from pathlib import Path

with Path(Path(__file__).parent, "input").open() as f:
    lines = [line.rstrip("\n") for line in f]

i_line = 0
total_token = 0

while i_line < len(lines) - 2:
    btn_a_x, btn_a_y = list(map(int, re.findall(r"\d+", lines[i_line + 0])))
    btn_b_x, btn_b_y = list(map(int, re.findall(r"\d+", lines[i_line + 1])))
    prize_x, prize_y = list(map(int, re.findall(r"\d+", lines[i_line + 2])))

    for b in range(0, prize_y // btn_b_y + 1):
        a = (prize_x - btn_b_x * b) / btn_a_x
        if a.is_integer():
            if btn_a_y * a + btn_b_y * b == prize_y:
                total_token += 3 * int(a) + b

    i_line += 4

print(f"Result: {total_token}")  # Result: 29598
