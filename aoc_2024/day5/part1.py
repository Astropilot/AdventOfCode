from pathlib import Path

with Path(Path(__file__).parent, "input").open() as f:
    lines = [line.rstrip("\n") for line in f]

delimiter = lines.index("")
total = 0
ordering_rules: list[list[str]] = [line.split("|") for line in lines[:delimiter]]

for line in lines[delimiter + 1 :]:
    update = line.split(",")

    update_correct = True
    for idx, page in enumerate(update):
        for rule in ordering_rules:
            if rule[0] == page and rule[1] in update:
                idx_after = update.index(rule[1])
                if idx > idx_after:
                    update_correct = False
            elif rule[1] == page and rule[0] in update:
                idx_before = update.index(rule[0])
                if idx < idx_before:
                    update_correct = False
        if update_correct is False:
            break

    if update_correct:
        total += int(update[len(update) // 2])

print(f"Result: {total}")
