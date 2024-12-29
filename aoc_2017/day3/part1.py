from pathlib import Path

goal = int(Path(Path(__file__).parent, "input").read_text())

i_steps = 0
current = 1
position = (0, 0)

while True:
    current += 1
    position = (position[0] + 1, position[1])
    i_steps += 1

    if current == goal:
        break

    for _ in range(i_steps):
        current += 1
        position = (position[0], position[1] - 1)
        if current == goal:
            break
    if current == goal:
        break
    i_steps += 1

    for _ in range(i_steps):
        current += 1
        position = (position[0] - 1, position[1])
        if current == goal:
            break
    if current == goal:
        break
    for _ in range(i_steps):
        current += 1
        position = (position[0], position[1] + 1)
        if current == goal:
            break
    if current == goal:
        break
    for _ in range(i_steps):
        current += 1
        position = (position[0] + 1, position[1])
        if current == goal:
            break
    if current == goal:
        break

print(f"Result: {abs(position[0]) + abs(position[1])}")
