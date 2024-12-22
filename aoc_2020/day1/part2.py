from pathlib import Path

with Path(Path(__file__).parent, "input").open() as f:
    expenses = [int(line.rstrip("\n")) for line in f]

result = None
for expense1 in expenses:
    for expense2 in expenses:
        if expense1 == expense2:
            continue
        for expense3 in expenses:
            if expense2 == expense3 or expense1 == expense3:
                continue
            if expense1 + expense2 + expense3 == 2020:
                result = expense1 * expense2 * expense3
                break
        if result is not None:
            break
    if result is not None:
        break

print(f"Result: {result}")  # Result: 236873508
