import math
from pathlib import Path
from queue import PriorityQueue

contents = Path(Path(__file__).parent, "input").read_text()
lines = contents.split("\n")


def get_neighbors(vertice: tuple[int, int]) -> list[tuple[int, int]]:
    neighbors: list[tuple[int, int]] = []
    for x, y in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
        x = vertice[0] + x
        y = vertice[1] + y
        if 0 <= x < len(lines[0]) and 0 <= y < len(lines):
            neighbors.append((x, y))
    return neighbors


def get_cost(v: tuple[int, int]) -> float:
    return int(lines[v[1]][v[0]])


start = (0, 0)
goal = (len(lines[0]) - 1, len(lines) - 1)
visited: set[tuple[int, int]] = set()
distance: dict[tuple[int, int], float] = {start: 0}
previous: dict[tuple[int, int], tuple[int, int]] = {}
Q: PriorityQueue[tuple[float, tuple[int, int]]] = PriorityQueue()


Q.put((0, start))

while Q:
    while not Q.empty():
        _, u = Q.get()
        if u not in visited:
            break
    else:
        break

    if u == goal:
        break

    visited.add(u)

    for v in get_neighbors(u):
        if v in visited:
            continue
        old_distance = distance.get(v, math.inf)
        new_distance = distance[u] + get_cost(v)

        if new_distance < old_distance:
            Q.put((new_distance, v))
            distance[v] = new_distance
            previous[v] = u

if goal not in previous:
    print("No path found!")
else:
    m: list[list[str]] = []
    heat_loss = 0

    for y in range(len(lines)):
        m.append([])
        for x in range(len(lines[y])):
            m[-1].append(lines[y][x])

    current: tuple[int, int] | None = goal

    while current is not None:
        if current != start:
            heat_loss += int(m[current[1]][current[0]])
        if current in previous:
            m[current[1]][current[0]] = "."
            current = previous[current]
        else:
            m[current[1]][current[0]] = "."
            current = None

    for y in range(len(m)):
        for x in range(len(m[y])):
            print(m[y][x], end="")
        print()

    print(f"Result {heat_loss}")  # Result:
