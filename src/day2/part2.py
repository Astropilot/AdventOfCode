import re
from pathlib import Path

contents = Path(Path(__file__).parent, "input").read_text()
sum_power = 0

for line in contents.split("\n"):
    colors_matchs = re.findall(r"((\d+) ([rgb]))", line)
    max_colors = {"r": 0, "g": 0, "b": 0}

    for color in colors_matchs:
        max_colors[color[2]] = max(max_colors[color[2]], int(color[1]))

    sum_power += max_colors["r"] * max_colors["g"] * max_colors["b"]

print(f"Result: {sum_power}")  # Result: 56322

# One liner (code golf for fun)
# fmt: off
print(sum([max(map(int,re.findall(r"(\d+) r",L)))*max(map(int,re.findall(r"(\d+) g",L)))*max(map(int,re.findall(r"(\d+) b",L)))for L in open("input")]))
# fmt: on
