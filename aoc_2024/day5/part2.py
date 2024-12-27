from pathlib import Path

with Path(Path(__file__).parent, "input").open() as f:
    lines = [line.rstrip("\n") for line in f]

delimiter = lines.index("")
total = 0
ordering_rules: list[list[str]] = [line.split("|") for line in lines[:delimiter]]

for line in lines[delimiter + 1 :]:
    update = line.split(",")
    rules_for_update = list(
        filter(lambda r: r[0] in update and r[1] in update, ordering_rules)
    )
    update_correct = True
    idx = 0
    while idx < len(update):
        page = update[idx]
        for rule in rules_for_update:
            if rule[0] == page:
                idx_after = update.index(rule[1])
                if idx > idx_after:
                    update_correct = False
                    update.remove(page)
                    update.insert(idx_after, page)
                    idx = 0
                    break

            elif rule[1] == page:
                idx_before = update.index(rule[0])
                if idx < idx_before:
                    update_correct = False
                    update.remove(page)
                    update.insert(idx_before + 1, page)
                    idx = 0
                    break
        idx += 1

    if update_correct:
        continue

    total += int(update[len(update) // 2])

print(f"Result: {total}")
