import re
from collections import Counter
from pathlib import Path

with Path(Path(__file__).parent, "input").open() as f:
    rooms = [line.rstrip("\n") for line in f]

total_sector_ids = 0

for room in rooms:
    m = re.match(r"([a-z-]+)-(\d+)\[([a-z]+)]", room)
    assert m is not None
    room_name = m.group(1).replace("-", "")
    sector_id = int(m.group(2))
    checksum = m.group(3)

    counter = Counter(room_name)
    keys = sorted(counter.keys())
    keys.sort(key=lambda k: counter[k], reverse=True)
    new_checksum = "".join(keys[:5])

    if new_checksum == checksum:
        total_sector_ids += sector_id

print(f"Result: {total_sector_ids}")
