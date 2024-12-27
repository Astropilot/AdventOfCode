from pathlib import Path

with Path(Path(__file__).parent, "input").open() as f:
    lines = [line.rstrip("\n") for line in f]

submarine: tuple[int, int] = (0, 0)

for line in lines:
    direction, count_str = line.split(" ")
    count = int(count_str)

    match direction:
        case "forward":
            submarine = (submarine[0] + count, submarine[1])
        case "down":
            submarine = (submarine[0], submarine[1] + count)
        case "up":
            submarine = (submarine[0], submarine[1] - count)
        case _:
            raise ValueError(f"Unknown direction: {direction}")

print(f"Result: {submarine[0] * submarine[1]}")
