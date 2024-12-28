from pathlib import Path

with Path(Path(__file__).parent, "input").open() as f:
    instructions = [line.rstrip("\n") for line in f]

DIRECTIONS = {
    "1": {"U": "1", "L": "1", "R": "2", "D": "4"},
    "2": {"U": "2", "L": "1", "R": "3", "D": "5"},
    "3": {"U": "3", "L": "2", "R": "3", "D": "6"},
    "4": {"U": "1", "L": "4", "R": "5", "D": "7"},
    "5": {"U": "2", "L": "4", "R": "6", "D": "8"},
    "6": {"U": "3", "L": "5", "R": "6", "D": "9"},
    "7": {"U": "4", "L": "7", "R": "8", "D": "7"},
    "8": {"U": "5", "L": "7", "R": "9", "D": "8"},
    "9": {"U": "6", "L": "8", "R": "9", "D": "9"},
}
code = ""
button = "5"

for instruction in instructions:
    for command in instruction:
        button = DIRECTIONS[button][command]
    code += button

print(f"Result: {code}")
