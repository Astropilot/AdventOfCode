from pathlib import Path

moves = Path(Path(__file__).parent, "input").read_text().split(",")

state = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p"]
ori_state = state.copy()
states = [state.copy()]
i = 1

while True:
    for move in moves:
        if move[0] == "s":
            shift = int(move[1:])
            for _ in range(shift):
                state.insert(0, state.pop())
        elif move[0] == "x":
            a, b = [int(n) for n in move[1:].split("/")]
            tmp = state[a]
            state[a] = state[b]
            state[b] = tmp
        elif move[0] == "p":
            c, d = move[1:].split("/")
            a = state.index(c)
            b = state.index(d)
            tmp = state[a]
            state[a] = state[b]
            state[b] = tmp

    if state == ori_state:
        break

    states.append(state.copy())
    i += 1

wanted_i = 1000000000 % i

print(f"Result: {''.join(states[wanted_i])}")
