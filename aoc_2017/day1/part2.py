from pathlib import Path

digits = [int(c) for c in Path(Path(__file__).parent, "input").read_text()]

sum_digits = 0
steps = len(digits) // 2

for i in range(len(digits)):
    next_i = (i + steps) % len(digits)
    if digits[i] == digits[next_i]:
        sum_digits += digits[i]

print(f"Result: {sum_digits}")
