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
    prize_x, prize_y = (prize_x + 10000000000000, prize_y + 10000000000000)

    determinant = btn_a_x * btn_b_y - btn_b_x * btn_a_y

    if determinant == 0:
        i_line += 4
        continue

    determinant_x = prize_x * btn_b_y - btn_b_x * prize_y
    determinant_y = btn_a_x * prize_y - prize_x * btn_a_y

    if determinant_x % determinant != 0 or determinant_y % determinant != 0:
        i_line += 4
        continue

    a = determinant_x // determinant
    b = determinant_y // determinant

    total_token += a * 3 + b

    i_line += 4

print(f"Result: {total_token}")
