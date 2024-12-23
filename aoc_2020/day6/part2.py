from pathlib import Path

with Path(Path(__file__).parent, "input").open() as f:
    lines = [line.rstrip("\n") for line in f]

i = 0
questions_answered: list[set[str]] = []
total_answers = 0

while i < len(lines):
    if lines[i] == "":
        answered = questions_answered[0]
        for people in questions_answered[1:]:
            answered = answered.intersection(people)
        total_answers += len(answered)
        questions_answered = []
        i += 1
        continue

    questions_answered.append(set(lines[i]))

    i += 1

answered = questions_answered[0]
for people in questions_answered[1:]:
    answered = answered.intersection(people)
total_answers += len(answered)

print(f"Result: {total_answers}")
