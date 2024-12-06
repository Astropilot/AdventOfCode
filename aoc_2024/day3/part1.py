import re
from pathlib import Path

contents = Path(Path(__file__).parent, "input").read_text()

print(sum(int(m[0]) * int(m[1]) for m in re.findall(r"mul\((\d+),(\d+)\)", contents)))

# Result: 160672468
