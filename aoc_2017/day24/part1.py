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
) -> int:
    strength = component[0] + component[1]

    max_strength_bridge = 0
    for c in [c for c in components if c[0] == component_out or c[1] == component_out]:
        components_copy = components.difference({c})
        c_out = c[1] if c[0] == component_out else c[0]
        max_strength_bridge = max(
            max_strength_bridge,
            compute_max_bridge(c, c_out, components_copy),
        )

    return strength + max_strength_bridge


max_strength_bridge = 0
for c in [c for c in components if c[0] == 0 or c[1] == 0]:
    components_copy = frozenset(components).difference({c})
    c_out = c[1] if c[0] == 0 else c[0]
    max_strength_bridge = max(
        max_strength_bridge, compute_max_bridge(c, c_out, components_copy)
    )

print(f"Result: {max_strength_bridge}")
