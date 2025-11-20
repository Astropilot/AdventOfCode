from pathlib import Path

polymer = list(Path(Path(__file__).parent, "input").read_text())
i = 0

while i < len(polymer) - 1:
    unit = polymer[i]
    reverse_unit = unit.swapcase()

    if polymer[i + 1] != reverse_unit:
        i += 1
    else:
        polymer.pop(i + 1)
        polymer.pop(i)
        i -= 1

print(len(polymer))
