import string
from pathlib import Path

polymer = Path(Path(__file__).parent, "input").read_text()

sizes: list[int] = []

for lower_letter in string.ascii_lowercase:
    polymer_copy = list(
        polymer.replace(lower_letter, "").replace(lower_letter.upper(), "")
    )

    i = 0
    while i < len(polymer_copy) - 1:
        unit = polymer_copy[i]
        reverse_unit = unit.swapcase()

        if polymer_copy[i + 1] != reverse_unit:
            i += 1
        else:
            polymer_copy.pop(i + 1)
            polymer_copy.pop(i)
            i -= 1

    sizes.append(len(polymer_copy))

print(min(sizes))
