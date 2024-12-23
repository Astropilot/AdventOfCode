from pathlib import Path

with Path(Path(__file__).parent, "input").open() as f:
    lines = [line.rstrip("\n") for line in f]

i = 0
questions_answered: set[str] = set()
total_answers = 0

while i < len(lines):
    if lines[i] == "":
        total_answers += len(questions_answered)
        questions_answered = set()
        i += 1
        continue

    questions_answered.update(lines[i])

    i += 1

total_answers += len(questions_answered)

print(f"Result: {total_answers}")
