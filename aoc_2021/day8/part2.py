from pathlib import Path

with Path(Path(__file__).parent, "input").open() as f:
    lines = [line.rstrip("\n") for line in f]

total_output = 0
for entry in lines:
    patterns_raw, output_raw = entry.split(" | ")
    patterns = [frozenset(p) for p in patterns_raw.split(" ")]
    output = [frozenset(o) for o in output_raw.split(" ")]

    digit_to_pattern: dict[int, frozenset[str]] = {}

    for pattern in patterns:
        if len(pattern) == 2:
            digit_to_pattern[1] = pattern
        elif len(pattern) == 4:
            digit_to_pattern[4] = pattern
        elif len(pattern) == 3:
            digit_to_pattern[7] = pattern
        elif len(pattern) == 7:
            digit_to_pattern[8] = pattern

    pattern_digit3 = next(
        p for p in patterns if len(p) == 5 and p.issuperset(digit_to_pattern[7])
    )
    digit_to_pattern[3] = pattern_digit3

    pattern_digit9 = next(
        p for p in patterns if len(p) == 6 and p.issuperset(digit_to_pattern[3])
    )
    digit_to_pattern[9] = pattern_digit9

    b_segment = next(iter(digit_to_pattern[9].difference(digit_to_pattern[3])))

    pattern_digit2 = next(
        p
        for p in patterns
        if len(p) == 5 and p != pattern_digit3 and b_segment not in p
    )
    digit_to_pattern[2] = pattern_digit2

    pattern_digit5 = next(
        p for p in patterns if len(p) == 5 and p not in digit_to_pattern.values()
    )
    digit_to_pattern[5] = pattern_digit5

    pattern_digit0 = next(
        p
        for p in patterns
        if len(p) == 6
        and p not in digit_to_pattern.values()
        and len(digit_to_pattern[8].difference(p)) == 1
        and p.issuperset(digit_to_pattern[1])
    )
    digit_to_pattern[0] = pattern_digit0

    pattern_digit6 = next(
        p for p in patterns if len(p) == 6 and p not in digit_to_pattern.values()
    )
    digit_to_pattern[6] = pattern_digit6

    pattern_to_digit = {v: k for k, v in digit_to_pattern.items()}
    output_str = ""
    for pattern in output:
        output_str += str(pattern_to_digit[pattern])

    total_output += int(output_str)

print(f"Result: {total_output}")  # Result: 989396
