from pathlib import Path

contents = Path(Path(__file__).parent, "input").read_text()
sum_calib = 0

for line in contents.split("\n"):
    numbers = list(filter(str.isdigit, line))
    sum_calib += int(numbers[0] + numbers[-1])

print(f"Result: {sum_calib}")
