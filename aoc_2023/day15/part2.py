import re
from pathlib import Path

contents = Path(Path(__file__).parent, "input").read_text()
contents = contents.strip("\n")


def hash_algo(s: str) -> int:
    current = 0

    for c in s:
        current += ord(c)
        current *= 17
        current = current % 256

    return current


boxes: dict[int, list[tuple[str, int]]] = {}

for i in range(256):
    boxes[i] = []

for step in contents.split(","):
    m = re.match(r"([a-z]+)(\=\d|-)", step)
    if m is None:
        print(f"ERROR on step {step}")
        break
    label, action = m.group(1), m.group(2)

    hash = hash_algo(label)

    if action == "-":
        boxes[hash] = list(filter(lambda lens: lens[0] != label, boxes[hash]))
    else:
        focal_length = int(action[-1])
        has_lens = False

        for idx, lens in enumerate(boxes[hash]):
            if lens[0] == label:
                boxes[hash][idx] = (label, focal_length)
                has_lens = True
                break
        if not has_lens:
            boxes[hash].append((label, focal_length))

sum_focusing_power = 0

for box_id, lenses in boxes.items():
    for lens_slot, lens in enumerate(lenses, 1):
        sum_focusing_power += (1 + box_id) * lens_slot * lens[1]

print(f"Result: {sum_focusing_power}")
