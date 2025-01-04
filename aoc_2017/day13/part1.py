import typing as t
from pathlib import Path

with Path(Path(__file__).parent, "input").open() as f:
    layers = [line.rstrip("\n") for line in f]

firewall_config: list[int | None] = []
firewall_state: list[tuple[int, t.Literal[1, -1]] | None] = []
packet_layer = -1

for layer_raw in layers:
    layer, length = [int(n) for n in layer_raw.split(": ")]

    if len(firewall_config) < layer:
        for _ in range(len(firewall_config), layer):
            firewall_config.append(None)
            firewall_state.append(None)
    firewall_config.append(length)
    firewall_state.append((0, 1))

severity = 0
while packet_layer != len(firewall_config) - 1:
    packet_layer += 1
    layer_state = firewall_state[packet_layer]

    if layer_state is not None and layer_state[0] == 0:
        severity += packet_layer * firewall_config[packet_layer]  # type: ignore

    for i in range(len(firewall_state)):
        layer_state = firewall_state[i]
        layer_config = firewall_config[i]

        if layer_state is None or layer_config is None:
            continue

        if layer_state[0] + layer_state[1] < 0:
            firewall_state[i] = (1, 1)
        elif layer_state[0] + layer_state[1] >= layer_config:
            firewall_state[i] = (layer_config - 2, -1)
        else:
            firewall_state[i] = (layer_state[0] + layer_state[1], layer_state[1])

print(f"Result: {severity}")
