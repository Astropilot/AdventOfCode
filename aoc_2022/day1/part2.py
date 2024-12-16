from pathlib import Path

with Path(Path(__file__).parent, "input").open() as f:
    lines = [line.rstrip("\n") for line in f]

calories: list[int] = []
sum_calories = 0

for line in lines:
    if len(line) == 0:
        calories.append(sum_calories)
        sum_calories = 0
        continue
    sum_calories += int(line)

calories.append(sum_calories)
calories.sort(reverse=True)
result = sum(calories[:3])

print(f"Result: {result}")  # Result: 206780