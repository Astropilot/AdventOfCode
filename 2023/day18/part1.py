from pathlib import Path

from shapely.geometry import Polygon  # type: ignore

contents = Path(Path(__file__).parent, "input").read_text()
lines = contents.split("\n")

current: tuple[int, int] = (0, 0)
points: list[tuple[int, int]] = [current]
nb_points = 2

for line in lines:
    data = line.split()
    direction, steps = data[0], int(data[1])

    nb_points += steps

    match direction:
        case "L":
            points.append((current[0] - steps, current[1]))
        case "R":
            points.append((current[0] + steps, current[1]))
        case "U":
            points.append((current[0], current[1] - steps))
        case "D":
            points.append((current[0], current[1] + steps))
        case _:
            print("ERROR")

    current = points[-1]

points = points[:-1]

poly = Polygon(points)  # type: ignore

total_size = (nb_points / 2) + poly.area  # type: ignore

print(f"Result: {total_size}")  # Result: 95356
