from pathlib import Path

pixels = [int(n) for n in Path(Path(__file__).parent, "input").read_text()]

IMAGE_WIDTH = 25
IMAGE_HEIGHT = 6
LAYER_PIXELS = IMAGE_WIDTH * IMAGE_HEIGHT

layer_count = len(pixels) // LAYER_PIXELS
layers: list[list[list[int]]] = [[] for _ in range(layer_count)]

for i, pixel in enumerate(pixels):
    row_i = (i // IMAGE_WIDTH) % IMAGE_HEIGHT
    layer_i = (i // IMAGE_WIDTH) // IMAGE_HEIGHT

    if len(layers[layer_i]) == row_i:
        layers[layer_i].append([])

    layers[layer_i][row_i].append(pixel)

lowest_layer: tuple[int, int] | None = None
for i, layer in enumerate(layers):
    sum_0 = sum(row.count(0) for row in layer)

    if lowest_layer is None or lowest_layer[1] > sum_0:
        lowest_layer = (i, sum_0)

assert lowest_layer is not None

r = sum(row.count(1) for row in layers[lowest_layer[0]]) * sum(
    row.count(2) for row in layers[lowest_layer[0]]
)

print(f"Result: {r}")
