from pathlib import Path

adj_list: dict[str, list[str]] = {}

with Path(Path(__file__).parent, "input").open() as f:
    orbits_raw = [line.rstrip("\n") for line in f]

for raw in orbits_raw:
    a, b = raw.split(")")
    adj_list.setdefault(a, []).append(b)


def count_orbits(obj: str, count: int = 0) -> int:
    c = 0

    if obj in adj_list:
        for next in adj_list[obj]:
            c += count_orbits(next, count + 1)

    return c + count


count = count_orbits("COM")

print(f"Result: {count}")
