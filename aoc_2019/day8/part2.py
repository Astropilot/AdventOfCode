from pathlib import Path

pixels = [int(n) for n in Path(Path(__file__).parent, "input").read_text()]

IMAGE_WIDTH = 25
IMAGE_HEIGHT = 6
LAYER_PIXELS = IMAGE_WIDTH * IMAGE_HEIGHT

image: list[list[int]] = [[2] * IMAGE_WIDTH for _ in range(IMAGE_HEIGHT)]

for i, pixel in enumerate(pixels):
    column_i = i % IMAGE_WIDTH
    row_i = (i // IMAGE_WIDTH) % IMAGE_HEIGHT

    if image[row_i][column_i] == 2:
        image[row_i][column_i] = pixel

for row in image:
    for pixel in row:
        print("#" if pixel == 1 else " ", end="")
    print()
