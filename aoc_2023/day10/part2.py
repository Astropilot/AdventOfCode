from pathlib import Path

contents = Path(Path(__file__).parent, "input").read_text()
lines = contents.split("\n")

adjacency_list: dict[tuple[int, int], list[tuple[int, int]]] = {}
start: tuple[int, int] = (0, 0)

for y in range(len(lines)):
    found = False
    for x in range(len(lines[y])):
        if lines[y][x] == "S":
            start = (x, y)
            found = True
            break
    if found:
        break

path_loop: list[tuple[int, int]] = [start]
finished = False

while not finished:
    x, y = path_loop[-1]
    current_node = lines[y][x]
    previous_direction = None

    if current_node != "S":
        if x < path_loop[-2][0]:
            previous_direction = "right"
        elif x > path_loop[-2][0]:
            previous_direction = "left"
        elif y < path_loop[-2][1]:
            previous_direction = "bottom"
        else:
            previous_direction = "up"

    match current_node:
        case "|":
            if previous_direction == "bottom":
                path_loop.append((x, y - 1))
            if previous_direction == "up":
                path_loop.append((x, y + 1))
        case "-":
            if previous_direction == "left":
                path_loop.append((x + 1, y))
            if previous_direction == "right":
                path_loop.append((x - 1, y))
        case "L":
            if previous_direction == "up":
                path_loop.append((x + 1, y))
            if previous_direction == "right":
                path_loop.append((x, y - 1))
        case "J":
            if previous_direction == "up":
                path_loop.append((x - 1, y))
            if previous_direction == "left":
                path_loop.append((x, y - 1))
        case "7":
            if previous_direction == "left":
                path_loop.append((x, y + 1))
            if previous_direction == "bottom":
                path_loop.append((x - 1, y))
        case "F":
            if previous_direction == "right":
                path_loop.append((x, y + 1))
            if previous_direction == "bottom":
                path_loop.append((x + 1, y))
        case ".":
            print("ERROR! Point detected")
        case "S":
            for x_dir, y_dir, pipes in [
                (-1, 0, ["-", "L", "F"]),
                (1, 0, ["-", "J", "7"]),
                (0, -1, ["|", "7", "F"]),
                (0, 1, ["|", "L", "J"]),
            ]:
                if 0 <= x + x_dir < len(lines[0]) and lines[y][x + x_dir] in pipes:
                    path_loop.append((x + x_dir, y))
                    break
                if 0 <= y + y_dir < len(lines) and lines[y + y_dir][x] in pipes:
                    path_loop.append((x, y + y_dir))
                    break
        case _:
            print(f"ERROR! Unknown {current_node} character detected!")

    if path_loop[-1] == start:
        finished = True

tiles_count = 0
founds: list[tuple[int, int]] = []

for y in range(len(lines)):
    nb_line = 0
    previous_direction = ""
    for x in range(len(lines[y])):
        if (x, y) in path_loop:
            match lines[y][x]:
                case "F" | "7":
                    if previous_direction == "up":
                        nb_line += 1
                        previous_direction = ""
                    elif previous_direction == "down":
                        previous_direction = ""
                    else:
                        previous_direction = "down"
                case "L" | "J":
                    if previous_direction == "down":
                        nb_line += 1
                        previous_direction = ""
                    elif previous_direction == "up":
                        previous_direction = ""
                    else:
                        previous_direction = "up"
                case "|":
                    nb_line += 1
                case _:
                    pass

            continue

        if nb_line % 2 == 1:
            founds.append((x, y))
            tiles_count += 1

print(f"Result: {tiles_count}")
