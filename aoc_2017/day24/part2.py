from functools import cache
from pathlib import Path

with Path(Path(__file__).parent, "input").open() as f:
    components_raw = [line.rstrip("\n") for line in f]

components: list[tuple[int, int]] = []

for component in components_raw:
    pin1, pin2 = [int(n) for n in component.split("/")]

    components.append((pin1, pin2))


@cache
def compute_max_bridge(
    component: tuple[int, int],
    component_out: int,
    components: frozenset[tuple[int, int]],
    length: int = 1,
) -> tuple[int, int]:
    strength = component[0] + component[1]

    candidates: list[tuple[int, int]] = []
    for c in [c for c in components if c[0] == component_out or c[1] == component_out]:
        components_copy = components.difference({c})
        c_out = c[1] if c[0] == component_out else c[0]
        candidates.append(compute_max_bridge(c, c_out, components_copy, length + 1))

    if len(candidates) == 0:
        return length, strength

    candidates.sort(key=lambda c: c[1], reverse=True)
    candidates.sort(key=lambda c: c[0], reverse=True)
    candidate = candidates[0]

    return candidate[0], strength + candidate[1]


candidates: list[tuple[int, int]] = []
for c in [c for c in components if c[0] == 0 or c[1] == 0]:
    components_copy = frozenset(components).difference({c})
    c_out = c[1] if c[0] == 0 else c[0]
    candidates.append(compute_max_bridge(c, c_out, components_copy))

candidates.sort(key=lambda c: c[1], reverse=True)
candidates.sort(key=lambda c: c[0], reverse=True)
candidate = candidates[0]

print(f"Result: {candidate[1]}")
