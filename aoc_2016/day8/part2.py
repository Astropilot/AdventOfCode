from pathlib import Path

with Path(Path(__file__).parent, "input").open() as f:
    instructions = [line.rstrip("\n") for line in f]

screen = [[0] * 50 for _ in range(6)]


for instruction in instructions:
    if instruction.startswith("rect"):
        arg = instruction.split(" ")[1]
        w, h = [int(n) for n in arg.split("x")]
        for y in range(h):
            for x in range(w):
                screen[y][x] = 1
    elif instruction.startswith("rotate row"):
        shift = int(instruction.split(" by ")[1])
        row = int(instruction.split(" by ")[0].split("=")[1])
        for _ in range(shift):
            screen[row].insert(0, screen[row].pop())
    elif instruction.startswith("rotate column"):
        shift = int(instruction.split(" by ")[1])
        column = int(instruction.split(" by ")[0].split("=")[1])
        column_data = [
            screen[0][column],
            screen[1][column],
            screen[2][column],
            screen[3][column],
            screen[4][column],
            screen[5][column],
        ]
        for _ in range(shift):
            column_data.insert(0, column_data.pop())
        screen[0][column] = column_data[0]
        screen[1][column] = column_data[1]
        screen[2][column] = column_data[2]
        screen[3][column] = column_data[3]
        screen[4][column] = column_data[4]
        screen[5][column] = column_data[5]

for l in screen:
    for c in l:
        if c == 1:
            print("#", end="")
        else:
            print(" ", end="")
    print()
