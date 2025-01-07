import re
import typing as t
from dataclasses import dataclass
from pathlib import Path


@dataclass
class State:
    name: str
    action_if_0: tuple[t.Literal[0, 1], t.Literal[1, -1], str]
    action_if_1: tuple[t.Literal[0, 1], t.Literal[1, -1], str]


with Path(Path(__file__).parent, "input").open() as f:
    instructions = [line.rstrip("\n") for line in f]

begin_state = instructions[0][-2]
steps_stop = int(re.search(r"\d+", instructions[1]).group(0))  # type: ignore
states: dict[str, State] = {}
tape: list[t.Literal[0, 1]] = [0]
cursor = 0


def move_cursor(tape: list[t.Literal[0, 1]], cursor: int) -> int:
    if cursor == -1:
        tape.insert(0, 0)
        return 0
    elif cursor == len(tape):
        tape.append(0)
    return cursor


for i in range(3, len(instructions), 10):
    state_name = instructions[i][-2]
    action_if_0 = (
        int(instructions[i + 2][-2]),
        -1
        if instructions[i + 3].removeprefix("    - Move one slot to the ")[:-1]
        == "left"
        else 1,
        instructions[i + 4][-2],
    )
    action_if_1 = (
        int(instructions[i + 6][-2]),
        -1
        if instructions[i + 7].removeprefix("    - Move one slot to the ")[:-1]
        == "left"
        else 1,
        instructions[i + 8][-2],
    )
    states[state_name] = State(state_name, action_if_0, action_if_1)  # type: ignore

current_state = states[begin_state]

for _ in range(steps_stop):
    action = (
        current_state.action_if_0 if tape[cursor] == 0 else current_state.action_if_1
    )

    tape[cursor] = action[0]
    cursor = move_cursor(tape, cursor + action[1])
    current_state = states[action[2]]

print(f"Result: {sum(tape)}")
