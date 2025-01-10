import itertools
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from aoc_2019.day7.intcode2 import ProgramState, execute_intcode

intcode_ori = [
    int(c) for c in Path(Path(__file__).parent, "input").read_text().split(",")
]

max_signal = 0

for sequence in itertools.permutations([5, 6, 7, 8, 9]):
    programs: list[ProgramState] = [
        ProgramState(0, 0, intcode_ori.copy(), False) for _ in range(len(sequence))
    ]
    signal = 0

    for i in range(len(sequence)):
        execute_intcode(programs[i], [sequence[i]])

    while any(not program.finished for program in programs):
        for i in range(5):
            output = execute_intcode(programs[i], [signal])
            signal = output[0]

    max_signal = max(max_signal, signal)

print(f"Result: {max_signal}")
