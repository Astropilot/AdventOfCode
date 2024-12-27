from pathlib import Path

with Path(Path(__file__).parent, "input").open() as f:
    lines = [line.rstrip("\n").split(" ") for line in f]

rules_win = {"A": "Y", "B": "Z", "C": "X"}
rules_loose = {"A": "Z", "B": "X", "C": "Y"}
rules_same = {"A": "X", "B": "Y", "C": "Z"}
score_hand = {"X": 1, "Y": 2, "Z": 3}
total_score = 0
for line in lines:
    opponent, result = line
    score = 0

    if result == "Z":
        score += 6
        score += score_hand[rules_win[opponent]]
    elif result == "Y":
        score += 3
        score += score_hand[rules_same[opponent]]
    else:
        score += score_hand[rules_loose[opponent]]

    total_score += score

print(f"Result: {total_score}")
