from pathlib import Path

with Path(Path(__file__).parent, "input").open() as f:
    lines = [line.rstrip("\n").split(" ") for line in f]

rules_win = {"A": "Y", "B": "Z", "C": "X"}
rules_same = {"A": "X", "B": "Y", "C": "Z"}
score_hand = {"X": 1, "Y": 2, "Z": 3}
total_score = 0
for line in lines:
    opponent, me = line
    score = score_hand[me]

    if rules_win[opponent] == me:
        score += 6
    elif rules_same[opponent] == me:
        score += 3

    total_score += score

print(f"Result: {total_score}")  # Result: 14163
