import sys
import typing as t
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from aoc_2019.day7.intcode2 import ProgramState, execute_intcode


class CoordsT(t.NamedTuple):
    x: int
    y: int


intcode = [int(c) for c in Path(Path(__file__).parent, "input").read_text().split(",")]
intcode[0] = 2
program = ProgramState(0, 0, intcode, False)

screen: dict[CoordsT, int] = {}
score = 0
joystick = 0
paddle_pos: CoordsT = CoordsT(0, 0)
ball_pos: CoordsT = CoordsT(0, 0)

output = execute_intcode(program, [])
for i in range(0, len(output), 3):
    c = CoordsT(output[i], output[i + 1])
    screen[c] = output[i + 2]

    if output[i + 2] == 3:
        paddle_pos = c
    elif output[i + 2] == 4:
        ball_pos = c

last_ball_pos = ball_pos

while not program.finished:
    output = execute_intcode(program, [joystick])

    for i in range(0, len(output), 3):
        if output[i] == -1 and output[i + 1] == 0:
            score = output[i + 2]
            continue
        c = CoordsT(output[i], output[i + 1])
        screen[c] = output[i + 2]

        if output[i + 2] == 3:
            paddle_pos = c
        elif output[i + 2] == 4:
            ball_pos = c

    direction_y = "up" if last_ball_pos.y > ball_pos.y else "down"
    direction_x = "left" if last_ball_pos.x > ball_pos.x else "right"

    destination_ball = ball_pos
    if direction_y == "down":
        while destination_ball.y != paddle_pos.y:
            delta_x = 1 if direction_x == "right" else -1
            destination_ball = CoordsT(
                destination_ball.x + delta_x, destination_ball.y + 1
            )

    if destination_ball.x < paddle_pos.x:
        joystick = -1
    elif destination_ball.x > paddle_pos.x:
        joystick = 1
    else:
        joystick = 0

    last_ball_pos = ball_pos

if any(c == 2 for c in screen.values()):
    print("[ERROR] Didn't win!!!")

print(f"Result: {score}")
