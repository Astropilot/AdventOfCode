import itertools
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from aoc_2019.day7.intcode import execute_intcode

intcode_ori = [
    int(c) for c in Path(Path(__file__).parent, "input").read_text().split(",")
]

max_signal = 0

for sequence in itertools.permutations([0, 1, 2, 3, 4]):
    signal = 0

    for i in range(5):
        intcode = intcode_ori.copy()
        output = execute_intcode(intcode, [sequence[i], signal])

        signal = output[0]

    max_signal = max(max_signal, signal)

print(f"Result: {max_signal}")
