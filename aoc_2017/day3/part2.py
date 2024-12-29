from pathlib import Path

goal = int(Path(Path(__file__).parent, "input").read_text())

i_steps = 0
position = (0, 0)
numbers_per_position: dict[tuple[int, int], int] = {(0, 0): 1}
current = 1


def get_sum_neighbors(position: tuple[int, int]) -> int:
    global numbers_per_position

    sum_neighbors = 0
    for dx, dy in (
        (0, -1),
        (1, -1),
        (1, 0),
        (1, 1),
        (0, 1),
        (-1, 1),
        (-1, 0),
        (-1, -1),
    ):
        neighbor = (position[0] + dx, position[1] + dy)
        sum_neighbors += numbers_per_position.get(neighbor, 0)

    numbers_per_position[position] = sum_neighbors
    return sum_neighbors


while True:
    position = (position[0] + 1, position[1])
    current = get_sum_neighbors(position)
    i_steps += 1

    if current > goal:
        break

    for _ in range(i_steps):
        position = (position[0], position[1] - 1)
        current = get_sum_neighbors(position)
        if current > goal:
            break
    if current > goal:
        break
    i_steps += 1

    for _ in range(i_steps):
        position = (position[0] - 1, position[1])
        current = get_sum_neighbors(position)
        if current > goal:
            break
    if current > goal:
        break

    for _ in range(i_steps):
        position = (position[0], position[1] + 1)
        current = get_sum_neighbors(position)
        if current > goal:
            break
    if current > goal:
        break

    for _ in range(i_steps):
        position = (position[0] + 1, position[1])
        current = get_sum_neighbors(position)
        if current > goal:
            break
    if current > goal:
        break

print(f"Result: {current}")
