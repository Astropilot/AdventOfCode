from pathlib import Path

moves = Path(Path(__file__).parent, "input").read_text().split(",")

state = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p"]

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

print(f"Result: {''.join(state)}")
