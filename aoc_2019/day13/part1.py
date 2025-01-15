import sys
import typing as t
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from aoc_2019.day7.intcode2 import ProgramState, execute_intcode


class CoordsT(t.NamedTuple):
    x: int
    y: int


intcode_ori = [
    int(c) for c in Path(Path(__file__).parent, "input").read_text().split(",")
]
program = ProgramState(0, 0, intcode_ori.copy(), False)

screen: dict[CoordsT, int] = {}
output = execute_intcode(program, [])

for i in range(0, len(output), 3):
    screen[CoordsT(output[i], output[i + 1])] = output[i + 2]

print(f"Result: {len([v for v in screen.values() if v == 2])}")
